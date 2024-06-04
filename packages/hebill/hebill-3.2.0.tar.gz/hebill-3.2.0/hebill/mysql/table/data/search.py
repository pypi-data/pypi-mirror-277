from ...table import Table
from ...plugins import Wheres as WheresClass, Limits as LimitsClass, Orders as OrdersClass, Columns as ColumnsClass


class Search:
    def __init__(self, table: Table):
        self._table = table
        self.query = table.query
        self.prefix = table.prefix
        self._wheres = None
        self._orders = None
        self._limits = None
        self._columns = None

    @property
    def wheres(self) -> WheresClass:
        if self._wheres is None:
            self._wheres = WheresClass()
        return self._wheres

    @property
    def columns(self) -> ColumnsClass:
        if self._columns is None:
            self._columns = ColumnsClass()
        return self._columns

    @property
    def orders(self) -> OrdersClass:
        if self._orders is None:
            self._orders = OrdersClass()
        return self._orders

    @property
    def limits(self) -> LimitsClass:
        if self._limits is None:
            self._limits = LimitsClass()
        return self._limits

    def single(self) -> dict | None:
        self.limits.start = 0
        self.limits.quantity = 1
        r = self.multiple()
        if len(r) < 1:
            return None
        return r[0]

    def multiple(self) -> list:
        sql = (
            f"SELECT {self.columns.output()} "
            f"FROM `{self._table.fullname}`"
            f"{self.wheres.output()}{self.orders.output()}{self.limits.output()}"
        )
        ero = f"检索数据表{self._table.fullname}数据发生错误：{{e}}"
        return self.query(sql, 'data')[1]

    def quantity(self):
        sql = (f"SELECT COUNT(*) FROM `{self._table.fullname}`"
               f"{self.wheres.output()}{self.orders.output()}{self.limits.output()}")
        ero = f"检索数据表{self._table.fullname}数据数量发生错误：{{e}}"
        return self.query(sql, 'quantity')[1]
