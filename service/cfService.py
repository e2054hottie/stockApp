from dao.expenseDao import ExpenseDao
from entity.Expense import Expense
import json 

def expense_to_dict(expense):
    return {
        "item": expense.item,
        "category": expense.category,
        "description": expense.description,
        "price": expense.price,
        "expense_date": str(expense.expense_date)
    }

class CfService:
    def __init__(self):
        self.expenseDao = ExpenseDao()
    
    def regist_expense(self,form,user_id):
        expens = Expense()
        
        expens.user_id = user_id
        expens.item = form["item"]
        expens.category = int(form["category"])
        expens.description = form["description"]
        expens.price = int(form["price"])
        expens.expense_date = form["expense_date"]
        
        self.expenseDao.insert(expens)
        print("ex")

    def get_expenses(self,user_id):
        result = self.expenseDao.select_wiht_name_by_user_id(int(user_id))
        
        return result