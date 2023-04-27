from . import Expense
import collections

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
print(spending_counter)

top5 = spending_counter.most_common(5)
print(top5)

categories, count = zip(*top5)
print(categories, count)

