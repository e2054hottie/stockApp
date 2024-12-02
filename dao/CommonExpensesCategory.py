from databaseMappingFlamework.databaseMapping import select

class CommonExpensesCategoryDao:
    @select("CommonExpensesCategory")
    def select_by_id(self,id):
        pass