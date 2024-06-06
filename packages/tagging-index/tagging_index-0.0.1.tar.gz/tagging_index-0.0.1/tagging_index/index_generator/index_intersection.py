from typing import Tuple, Type
import pandas as pd
from odps import ODPS
from odps.inter import enter
from .common_index_generator import CommonIndexGenerator, IndexSqlTemplate


class IndexIntersection:
    def __init__(self, index_generator: CommonIndexGenerator):
        self.index_generator = index_generator

    def _generate_sql(self, index_codes: Tuple[str, str], return_result=False):
        index1 = self.index_generator.get_index_sql_template(index_codes[0])
        index2 = self.index_generator.get_index_sql_template(index_codes[1])
        intersection_sql = f"""
        (select a.* from {index1.sql_source_tag_data} a left semi join {index2.sql_source_tag_data} b
        on a.entity_id=b.entity_id)
        """
        index_x_template = IndexSqlTemplate(
            index1.sql_comp_map,
            intersection_sql,
            index1.sql_year_sequence,
            index1.index_version,
            index1.comp_type,
            f"X_{index_codes[0]}_{index_codes[1]}",
            f"X_{index1.index_name}_{index2.index_name}",
            self.index_generator.DWD_TABLE,
        )
        sql_template = (
            index1.INDEX_TEMPLATE_SELECT
            if return_result
            else index1.INDEX_TEMPLATE_INSERT
        )
        sql = sql_template.format(**index_x_template.__dict__)
        return sql

    @property
    def o(self) -> ODPS:
        return enter().odps

    def get_index_data(self, index_codes: Tuple[str, str]) -> pd.DataFrame:
        """return specified index data in dataframe rather than insert into table

        Args:
            index_code (str)

        Returns:
            pd.DataFrame:
        """
        sql = self._generate_sql(index_codes, return_result=True)
        df = (
            self.o.execute_sql(sql, hints={"odps.sql.submit.mode": "script"})
            .open_reader()
            .to_pandas(count=100)
        )
        return df
