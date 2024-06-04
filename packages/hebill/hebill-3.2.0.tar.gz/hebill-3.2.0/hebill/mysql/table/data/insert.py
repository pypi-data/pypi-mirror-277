from datetime import datetime
import uuid
from ...table import Table


class Insert:
    def __init__(self, table: Table):
        self._table = table

    def single(self, data: dict, user: str = 0, keywords: str | list = '') -> bool:
        if not data:
            return False
        # data["_id"]
        data["_sn"] = str(uuid.uuid4())
        data["_order"] = 0
        if keywords is not None:
            if isinstance(keywords, str):
                data["_keywords"] = keywords
            elif isinstance(keywords, list):
                data["_keywords"] = ' '.join(keywords)
        data["_created_by"] = user
        data["_created_date"] = int(datetime.now().timestamp() // 1)
        str_key_array = [f'`{key}`' for key in data]
        str_value_array = [f'"{value}"' for value in data.values()]
        sql = (f'INSERT INTO `{self._table.fullname}` ({", ".join(str_key_array)})'
               f' VALUES ({", ".join(str_value_array)});')
        inserted_id = self._table.query(sql, 'insert')[1]
        if inserted_id < 1:
            return False
        update = self._table.data.update
        update.wheres.add_condition('_id', inserted_id)
        update.multiple({'_order': inserted_id})
        return True

    def multiple(self, data_list: list) -> bool:
        if not data_list:
            return False

        return all(self.single(data) for data in data_list)
