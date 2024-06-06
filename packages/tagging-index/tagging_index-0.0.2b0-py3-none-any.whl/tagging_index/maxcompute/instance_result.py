from typing import Dict, List, Mapping, NamedTuple


class InstanceResult:
    """
    instance的原始运行结果
        `inputs` 运行日志解析得到的运行过程输入资产信息, eg. {"table_name": {size:0, rows:0}}
        `outputs` 运行日志解析得到的运行过程输出资产信息, eg. {"table_name": {size:0, rows:0}}
        `cost` 运行日志解析得到的任务消耗 eg. {cost_cpu: 0, cost_memory: 0}
        `result` 运行日志解析的打印日志
        `details` 运行日志解析得到的其他详情, 如运行时间, 成功失败等
        `update_cost_result()`: 类方法, 合并多个数据任务的cost信息
        `merge_io_results()`: 类方法, 合并多个数据任务的输入输出数据
    """

    class TableStat(NamedTuple):
        rows: int
        size: int

    class TaskCost(NamedTuple):
        cost_cpu: int
        cost_memory: int

    def __init__(
        self,
        inputs: Mapping[str, TableStat] = {},
        outputs: Mapping[str, TableStat] = {},
        cost: TaskCost = TaskCost(0, 0),
        result: List[str] = [],
        details: Mapping = {},
    ):
        self.__inputs = inputs
        self.__outputs = outputs
        self.__cost = cost
        self.__result = result
        self.__details = details

    @property
    def inputs(self) -> Mapping[str, TableStat]:
        return self.__inputs

    @property
    def outputs(self) -> Mapping[str, TableStat]:
        return self.__outputs

    @property
    def cost(self) -> TaskCost:
        return self.__cost

    @property
    def result(self) -> List[str]:
        return self.__result

    @property
    def details(self) -> Mapping:
        return self.__details

    @classmethod
    def update_cost_result(cls, raw_cost: TaskCost, cost_info: TaskCost) -> TaskCost:

        new_cost_info = cls.TaskCost(
            raw_cost.cost_cpu + cost_info.cost_cpu,
            raw_cost.cost_memory + cost_info.cost_memory,
        )
        return new_cost_info

    @classmethod
    def merge_io_results(
        cls, raw_io: Dict[str, TableStat], io_info: Dict[str, TableStat]
    ):

        for key in raw_io:
            if key not in io_info:
                io_info[key] = cls.TableStat(0, 0)
            else:
                new_io_info = cls.TableStat(
                    raw_io[key].rows + io_info[key].rows,
                    raw_io[key].size + io_info[key].size,
                )
                io_info[key] = new_io_info
        return io_info
