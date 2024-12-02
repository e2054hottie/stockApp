select expenses.item as item, 
    common_expenses_category.category_name as category, 
    expenses.description as description,
    expenses.price as price,
    expenses.expense_date as expense_date
from expenses 
join common_expenses_category on 
expenses.category = common_expenses_category.id
where user_id = /* user_id */