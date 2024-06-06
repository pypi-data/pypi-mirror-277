from datetime import datetime, timedelta
import json
from typing import Dict, List, Mapping, Optional
from .instance_result import InstanceResult
from .initialize_maxcompute import _maxcompute_setup as mc
from odps.models import Instance
from odps import ODPS


class SqlRunner:
    """
    DataSubTask是一个可运行的ODPS任务的抽象类
        `script` 任务脚本
        `instance` 根据创建任务类型,返回odps对应实例,sql返回Instance,security返回{}
        `taskRunner` 任务运行需要的ODPS实例
        `is_wait` 任务是否允许同步执行True or 异步执行 False
        `is_terminated()` 方法用于获取该任务是否结束
        `is_successful()` 方法用于获取该任务是否成功
        `get_task_result()` 方法用于获取该任运行后的详情, 统一接口 TaskResult
    """

    def __init__(self, is_waited: bool, script: str, **kwargs):
        self.__script = script
        self.__is_waited = is_waited
        # 运行结果容器, 在子类run方法中被赋值, 跟odps类型绑定, 当前支持返回Instance或者{}
        self.instance: Optional[Instance] = None
        # 运行状态, none 还未运行, false 运行中, true 运行结束, 通过is_terminated访问
        self.__terminated: Optional[bool] = None
        # 运行结果, none 还未运行, false 运行失败, true 运行成功, 通过is_successful访问
        self.__successful: Optional[bool] = None
        # 用于记录是否刷新过任务结果
        self.__is_updated: Optional[bool] = None
        # 任务输入、输出等解析结果, 通过get_task_result访问
        self.__result = InstanceResult()
        self.hints = kwargs["hints"] if "hints" in kwargs else None

    @property
    def is_waited(self) -> bool:
        """是否同步任务"""
        return self.__is_waited

    @property
    def script(self) -> str:
        """脚本内容"""
        return self.__script

    @property
    def taskRunner(self):
        """运行环境"""
        return mc().default_odps

    def is_terminated(self) -> Optional[bool]:
        """
        运行状态 none 还未运行, false 运行中, true 运行结束
        """
        # 如果self.__terminated=True则不再更新
        if not self.__terminated:
            if isinstance(self.instance, dict):
                self.__terminated = True
            elif isinstance(self.instance, Instance):
                self.__terminated = self.instance.is_terminated()
        return self.__terminated

    def is_successful(self) -> Optional[bool]:
        """
        运行结果 none 未运行结束, false 运行失败, true 运行成功
        """
        # 如果self.__successful已赋值则不再更新
        if self.__successful is None:
            if self.is_terminated() == True:
                if isinstance(self.instance, Instance):
                    self.__successful = self.instance.is_successful()
                elif isinstance(self.instance, dict):
                    # 授权任务 成功返回{} 失败返回{'result':error_message}
                    self.__successful = False if self.instance else True
        return self.__successful

    def get_task_result(self):
        """
        单个任务进程运行结果
        """
        # 任务完成初始化任务结果,仅更新一次
        if self.is_terminated() == True and self.__is_updated == None:
            if isinstance(self.instance, Instance):
                self.__result = self.__parse_odps_instance()
            elif isinstance(self.instance, Dict):
                self.__result = InstanceResult(result=[self.instance.get("result")])  # type: ignore
            self.__is_updated = True
        return self.__result

    def __parse_odps_instance(self) -> InstanceResult:

        details = self.__check_instance_info()
        outputs = self.__update_io_result(details["instance_detail"]["Outputs"], {})
        inputs = self.__update_io_result(details["instance_detail"]["Inputs"], {})
        result = details["instance_detail"]["Result"]
        cost = details["instance_detail"]["Cost"]

        return InstanceResult(
            inputs=inputs, outputs=outputs, cost=cost, result=result, details=details
        )

    def __update_io_result(
        self, raw_io: Mapping[str, List[int]], io_info: Mapping[str, List[int]]
    ) -> Mapping[str, InstanceResult.TableStat]:
        """
        分区表解析时解析至一级分区为guid, 其他解析至表名即可
        input: 如果是分区表, 所有分区是一个key
            eg. ant_lhadb.lha_dim_np_id_convert_md/pt=20210531/domain_entity_type=onl_2c_spl/biz_source=taobao
                -> ant_lhadb.lha_dim_np_id_convert_md
        output: 如果是分区表, 每个分区是一个key, 取一级分区作为标准guid
            eg. ant_lhadb.lha_dwd_np_label_var_chain/ofl_label_id=SPL.ONL.CMN.0001A/current_status=N
                -> ant_lhadb.lha_dwd_np_label_var_chain

        Args:
            raw_io: 子任务的实例运行结果信息outputs/inputs,格式为{"tablename":[int,int],...}
            io_info: 原有的信息,将从raw_io中提取后并入

        Returns:
            dict:{"table_guid":{"rows":, "size":}}
        """
        for key in raw_io:
            table_name = key.split(",")[0].split("/")[0]
            io_stat = (
                {"rows": io_info[table_name][0], "size": io_info[table_name][1]}
                if table_name in io_info
                else {"rows": 0, "size": 0}
            )

            io_stat["rows"] += raw_io[key][0]
            io_stat["size"] += int(raw_io[key][1])
            io_info[table_name] = list(io_stat.values())  # type: ignore
        return io_info  # type: ignore

    def __check_instance_info(self):
        """
        获取instance对象的相关信息

        Returns:
            (dict)
                id (string): id
                logview (string): logview_address
                is_terminated (bool): 是否执行完成
                is_successful (bool): 是否执行成功
                start_time (datetime.datetime): 启动时间 -> 北京时间
                end_time (datetime.datetime): 结束时间(如果结束,否则None) -> 北京时间
                execute_time (string): 总耗时%H:%M:%S(如果结束,否则None)
                sub_tasks_detail (dict): 子任务详情
        """
        if self.instance:
            instance_details = {}
            instance_details["id"] = self.instance.id
            instance_details["logview"] = self.instance.get_logview_address()
            instance_details["is_terminated"] = self.instance.is_terminated()
            instance_details["is_successful"] = self.instance.is_successful()
            instance_details["start_time"] = self.instance.start_time + timedelta(
                hours=8
            )  # type: ignore
            instance_details["end_time"] = (
                self.instance.end_time + timedelta(hours=8)  # type: ignore
                if self.instance.is_terminated()
                else None
            )
            instance_details["execute_time"] = str(
                self.instance.end_time - self.instance.start_time  # type: ignore
            ).split(".")[
                0
            ]  # type: ignore
            instance_details["instance_detail"] = self.__merge_sub_tasks_detail()

            return instance_details

        return {}

    def __merge_sub_tasks_detail(self):
        """
        从instance对象中获取所有task信息

        Returns:
            (dict):
                key: task_name
                value:
                    Inputs-输入表, eg. {"alifin_assetm.alb_di_huabei_agdscc_user_credit_dd/dt=20170630,...45": [17641131560,158648030299]},
                    Outputs-输出表详情(dict), eg. {"antluohan_dev.pmt_obs_huabei_agdscc_user_credit_dd_smp/dt=20170630": [90041, 722679]}
                    OutputsDetail-输出表信息(历史版本, 无效信息删除):
                        eg. 动态分区插入 {"antluohan_dev.pmt_obs_huabei_agdscc_user_credit_dd_smp": {"isDynamicPartition": true}
                            静态分区插入 {"antluohan_dev.daipaotest2/dt=2020": {"isDynamicPartition": false}}
                            非分区表 {"antluohan_dev.daipaotest3": {"isDynamicPartition": false}}
                    Result-控制台输出(select或者报错), eg. ["", ""]
                    Cost-任务运行内存及cpu成本, {"cpu_cost":, "memory_cost":}
        """
        sub_tasks_detail = {
            "Inputs": {},
            "Outputs": {},
            "Result": [],
            "Cost": InstanceResult.TaskCost(0, 0),
        }
        if self.instance:
            for task in self.instance.get_task_names():

                # 如果没有print 或者 错误信息 返回空字符串''
                result = self.instance.get_task_result(task)
                sub_tasks_detail["Result"].append(result)
                detail = self.instance.get_task_detail2(task)
                if "mapReduce" in detail:
                    summary = json.loads(detail["mapReduce"].get("jsonSummary"))
                    if summary:
                        sub_tasks_detail["Inputs"].update(summary.get("inputs", {}))
                        sub_tasks_detail["Outputs"].update(summary.get("outputs", {}))
                        raw_cost = InstanceResult.TaskCost(
                            summary.get("cost_cpu") or 0,
                            summary.get("cost_memory") or 0,
                        )
                        sub_tasks_detail["Cost"] = InstanceResult.update_cost_result(
                            raw_cost, sub_tasks_detail["Cost"]
                        )
        return sub_tasks_detail

    def run(self):
        if self.hints:
            self.instance = self.taskRunner.execute_sql(self.script, hints=self.hints)
        else:
            self.instance = self.taskRunner.execute_sql(self.script)
