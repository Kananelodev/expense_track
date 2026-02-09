class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description



    def add_expense(self):
        add = {
             
        }

        

        



    def store(self):
        #I have to store and preferrably display the expenses


        store = {}
        data = ["Expense"]
        
        for categ, count in enumerate(data, start=1):
                
                store[categ] = {
                    'amount': self.amount,
                    'category': self.category,
                    'description': self.description,
                }
        print(store)
        return store
    
    
             




ok = Expense(50, "Food", "More food to buy")
wow = ok.store()
print(wow)


