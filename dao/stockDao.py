from databaseMappingFlamework.databaseMapping import select

class StockDao:
    @select("Stock")
    def insert(self,stock):
        pass

    @select("Stock")
    def select_by_id(self,id):
        pass