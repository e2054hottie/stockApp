from dao.stockDao import StockDao
from entity.Stock import Stock



class AssetManagementService:
    def __init__(self):
        self.stockDao = StockDao()
    
    def regist(self,form,id):
        stock = Stock()
        stock.code = form["code"]
        stock.user_id = id
        stock.acquisition_price = form["acquisition_price"]
        stock.quantity = form["quantity"]

        self.stockDao.insert(stock)
    
    def getStockData(self,id):
        result = self.stockDao.select_by_id(int(id))
        print(result)
        return result