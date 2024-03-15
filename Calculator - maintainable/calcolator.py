import utils

class Calculator:
    def __init__(self):
        self.operations = utils.load_operations()
    
    def calculate(self,num1,num2,operator):
        if operator in self.operations:
            return self.operations[operator](num1,num2)
        else:
            print("operator not found")
            return False