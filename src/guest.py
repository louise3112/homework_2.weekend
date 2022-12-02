class Guest():
    
    def __init__(self, input_name, input_age, input_money):
        self.name = input_name
        self.age = input_age
        self.money = input_money
    
    def decrease_money(self, amount):
        self.money -= amount
    
