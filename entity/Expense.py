from entity.auto_str import auto_str

@auto_str
class Expense:
    def __init__(self):
        self.id  = None
        self.user_id  = None
        self.item  = None
        self.category  = None
        self.description  = None
        self.price = None
        self.expense_date = None 
        self.created_at = None