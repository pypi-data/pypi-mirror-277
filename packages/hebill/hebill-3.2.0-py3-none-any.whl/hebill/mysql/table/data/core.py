class Data:
    def __init__(self, table):
        self._table = table

    @property
    def drop(self):
        from .drop import Drop
        return Drop(self._table)

    @property
    def insert(self):
        from .insert import Insert
        return Insert(self._table)

    @property
    def search(self):
        from .search import Search
        return Search(self._table)

    @property
    def update(self):
        from .update import Update
        return Update(self._table)

