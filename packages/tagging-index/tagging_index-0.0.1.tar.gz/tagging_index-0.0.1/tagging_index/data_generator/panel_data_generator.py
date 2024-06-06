from dataclasses import dataclass, field
from typing import Dict, List, Optional
from odps import ODPS
from odps.inter import enter


@dataclass
class VariableMap:
    code: str
    column_name: Optional[str] = field(default=None)
    """if not provide, use code as column_name"""


@dataclass
class VariableMapOther:
    source_data: str
    """ the table or sql for source data, sql should bracket off """
    source_var_col: str
    var_col_name: Optional[str] = field(default=None)
    """if not provide, use source_var_col as var_col_name"""
    dim_comp_id: str = "comp_id"
    col_comp_id: str = "comp_id"
    col_year: Optional[str] = field(default=None)
    """ none for non-time sequence variable """


class PanelDataGenerator:

    def __init__(self):
        self.index_version = "v1_ai_and_data"
        self.index_dwd_table = "ads_digital_talent_index"
        self.matrix_dwd_table = "dwd_cn_lst_com_measure"
        self.dim_comp_table = """
        ( 
                SELECT full_stock_id as comp_id
                ,stock_id
                ,nvl(abbr_cn,company_name_cn) company_abbr
                ,industry_level1 as industry_name
                FROM dim_china_listed_company 
                WHERE pt = MAX_PT('dim_china_listed_company')
        )
        """
        self._index_var: List[VariableMap] = []
        self._matrix_var: List[VariableMap] = []
        self.start_year = 2016
        self.end_year = 2020
        self._other_var: Dict[str, VariableMapOther] = {}
        self.comp_ids = []
        """empty for all comp_ids, default is all comp_ids"""

    def _get_index_cols(self):
        return ",".join([x.column_name or x.code for x in self._index_var])

    def _get_index_fields(self):
        return "\n,".join(
            f"'{x.code}' as {x.column_name or x.code}" for x in self._index_var
        )

    def _get_matrix_fields(self):
        return "\n,".join(
            f"'{x.code}' as {x.column_name or x.code}" for x in self._matrix_var
        )

    def _get_matrix_cols(self):
        return ",".join([x.column_name or x.code for x in self._matrix_var])

    def _get_matrix_codes(self):
        return ",".join([f"'{x.code}'" for x in self._matrix_var])

    def add_index(self, code: str, column_name: Optional[str] = None):
        """add index data to panel

        Args:
            code (str): index code to add to panel's variable
            column_name (Optional[str], optional): if not provide, use code as column_name. Defaults to None.
        """
        self._index_var.append(VariableMap(code, column_name))

    def add_matrix(self, code: str, column_name: Optional[str] = None):
        self._matrix_var.append(VariableMap(code, column_name))

    def _get_com_year_squence_sql(self):
        return f"""(select /*+ MAPJOIN(y) */ * from 
        {self.dim_comp_table} a join {self._get_year_sequence()} y
        where {self._get_comp_condition()}
        )"""

    def _get_index_sql(self):
        sql = f"""(
        SELECT comp_id,eff_year,{self._get_index_cols()} from
        ( select * from {self.index_dwd_table}  
            where index_version = '{self.index_version}'  
            and eff_year in {self._get_year_sequence()} and {self._get_comp_condition()} )
        pivot (max(index_value) for index_name IN ({self._get_index_fields()}))
        )
        """
        return sql

    def _get_matrix_sql(self):

        sql = f"""(
            SELECT comp_id,eff_year,{self._get_matrix_cols()} from 
            (select full_stock_id as comp_id,eff_year,source_code,measure_value from {self.matrix_dwd_table} 
             where eff_year in {self._get_year_sequence()} 
             and {self._get_comp_condition("full_stock_id")}
             and source_code in ({self._get_matrix_codes()})
            )
            pivot (max(measure_value) for source_code IN ({self._get_matrix_fields()}))
            )
        """
        return sql

    def _get_year_sequence(self):
        return f"(SELECT EXPLODE(SEQUENCE({self.start_year},{self.end_year})) as (eff_year))"

    def _get_comp_condition(self, comp_id_col="comp_id"):
        return (
            f""" {comp_id_col} in ({','.join([f"'{x}'" for x in self.comp_ids])})"""
            if self.comp_ids
            else "1=1"
        )

    def get_panel_sql(self):
        other_vars = self._get_other_var_sql()
        other_vars_join = "\n".join(
            [""]
            + [
                f"""left join {x} as {v} on {v}.comp_id = a.comp_id {f'and {v}.eff_year = a.eff_year' 
                if self._other_var[v].col_year else ''}"""
                for v, x in other_vars.items()
            ]
        )
        other_vars_cols = "\n,".join([f"{v}.{v}" for v, _ in other_vars.items()])
        sql = f""" select a.comp_id,a.eff_year,a.company_abbr,a.industry_name
        ,{self._get_matrix_cols()}
        ,{self._get_index_cols()}
        {','+other_vars_cols if other_vars_cols else ''}
        from {self._get_com_year_squence_sql()} a
        left join {self._get_index_sql()} b 
        on a.comp_id =b.comp_id and a.eff_year=b.eff_year
        left join {self._get_matrix_sql()} c
        on a.comp_Id = c.comp_id and a.eff_year=c.eff_year
        {other_vars_join}
        ;
        """
        return sql

    def add_other_var(self, var_map: VariableMapOther):
        if self._other_var.get(var_map.var_col_name or var_map.source_var_col):
            raise Exception(
                f"other var {var_map.var_col_name or var_map.source_var_col} already exists"
            )
        self._other_var[var_map.var_col_name or var_map.source_var_col] = var_map

    def _get_other_var_sql(self):
        other_var_sql: Dict[str, str] = {}
        for x, v in self._other_var.items():
            eff_year = f" a.{v.col_year} as eff_year," if v.col_year else ""
            where = (
                f" where  {v.col_year} in {self._get_year_sequence()}"
                if v.col_year
                else ""
            )
            other_var_sql[x] = (
                f"""(
            SELECT  b.comp_id,{eff_year}a.{x}
            from (
                select {v.col_comp_id},{v.col_year+',' if v.col_year else ""}{v.source_var_col} as {x} from {v.source_data} {where}
            ) a join {self.dim_comp_table} b on {v.col_comp_id} = b.{v.dim_comp_id})
            """
            )
        return other_var_sql

    @property
    def o(self) -> ODPS:
        return enter().odps

    def get_result_df(self):
        sql = self.get_panel_sql()
        result = (
            self.o.execute_sql(sql, hints={"odps.sql.submit.mode": "script"})
            .open_reader()
            .to_pandas()
        )
        return result

    def save_to_csv(self, path):
        df = self.get_result_df()
        df.to_csv(path, index=False)
