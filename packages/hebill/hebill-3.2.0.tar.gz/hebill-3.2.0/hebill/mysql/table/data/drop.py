from ...table import Table
from ...plugins import Wheres as WheresClass, Limits as LimitsClass, Orders as OrdersClass


class Drop:
    def __init__(self, table: Table):
        self._table = table
        self.query = table.query
        self.prefix = table.prefix
        self._wheres = None
        self._orders = None
        self._limits = None

    @property
    def wheres(self) -> WheresClass:
        if self._wheres is None:
            self._wheres = WheresClass()
        return self._wheres

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

    def all(self):
        sql = f'DELETE FROM {self._table.fullname}'
        ero = f'删除所有数据表{self._table.name}全部数据发生错误：{{e}}'
        return self.query(sql, ero)[1]

    def single(self):
        self.limits.start = 0
        self.limits.quantity = 1
        sql = f'DELETE FROM `{self._table.fullname}` ' + self.wheres.output() + self.limits.output()
        ero = f'删除数据表{self._table.name}单条数据发生错误：{{e}}'
        return self.query(sql, ero)[1]

    def multiple(self):
        sql = f'DELETE FROM `{self._table.fullname}` ' + self.wheres.output() + self.limits.output()
        ero = f'删除数据表{self._table.name}单(多)条数据发生错误：{{e}}'
        return self.query(sql, ero)[1]
