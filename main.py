import json
import os

class Expense:
    def __init__(self):
        pass
    
    def add_expense(self, amo, cat, desc):
        
        next_id = max(self.storing.keys()) + 1 if self.storing else 1
        self.storing[next_id] = {
        'amount': amo,
        'category': cat,
        'description': desc
        }
        return self.storing


        

        



    def store(self):
        #I have to store and preferrably display the expenses
        well = self.add_expense(self.amount, self.category, self.description)
    
        data = ["Expense"]
        
        for categ, count in enumerate(data, start=1): 
            self.storing[categ] = {
                'amount': self.amount,
                'category': self.category,
                'description': self.description,
            }

        return self.storing
    
    
             




ok = Expense(50, "Food", "More food to buy")
wow = ok.store()
print(wow)


