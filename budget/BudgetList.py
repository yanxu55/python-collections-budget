class BudgetList(list):
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []


    # Path: corepy/python-collections-budget/budget/BudgetList.py
    def append(self, item):
        if self.sum_expenses + item < self.budget:
            # Path: corepy/python-collections-budget/budget/BudgetList.py
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            # Path: corepy/python-collections-budget/budget/BudgetList.py
            self.overages.append(item)
            self.sum_overages += item


    def __len__(self):
        return len(self.expenses) + len(self.overages)
    
