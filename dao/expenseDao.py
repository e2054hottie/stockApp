from databaseMappingFlamework.databaseMapping import select

class ExpenseDao:
    @select("Expense")
    def insert(self,expense):
        pass

    @select("Expense",defaultSQL="select * from expenses")
    def select_all(self):
        pass