from typing import Optional, List


class SelectQuery:
    def __init__(self, table:str, columns: Optional[List[str]]="*", predicates: Optional[str]=None):
        self.sql = f"select {columns} from {table} {predicates};"


class AdministrativeDivisionQuery(SelectQuery):
    def __init__(self, dynastic_id:int):
        predicates = f"WHERE belongs5_ID={dynastic_id} or belongs4_ID={dynastic_id} or belongs3_ID={dynastic_id} or belongs2_ID={dynastic_id} or belongs1_ID={dynastic_id}"
        super().__init__(table="ADDRESSES", predicates=predicates)
        print(self.sql)
