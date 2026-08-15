class CalculateValue:
    def __init__(self, a:int, b:int):
        self.a = a
        self.b = b
        print("I am a constructor")
        # self.__sum()
        # self._multiply()
        # self._sub()

    def __sum(self):
        self.sum_value = self.a+self.b
        print(f'sum of the input is {self.sum_value}')

    def _multiply(self):
        print(f'product value is {self.a*self.b}')

    def _sub(self):
        print(f'Subtraction value is {self.a-self.b}')

    def calculate(self, operation):
        if operation == 'sum':
            self.__sum()
        elif operation == 'sub':
            self._sub()
        elif operation == 'mul':
            self._multiply()

obj1 = CalculateValue(5, 6) # Object creation
obj1.calculate('sum')
print("-----------------------------------")
obj2 = CalculateValue(1,2)
obj2.calculate('mul')
# obj.sum_value