from databaseMappingFlamework.databaseMapping import select

class ExpenseDao:
    @select("Expense")
    def insert(self,expense):
        pass

    @select("Expense",defaultSQL="select * from expenses")
    def select_all(self):
        pass

    @select("Expense")
    def select_by_user_id(self,id):
        pass

    @select("Expense")
    def select_wiht_name_by_user_id(self,user_id):
        pass