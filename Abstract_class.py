from abc import ABC, abstractmethod
class properties(ABC) :
    def salesPrice(self,amount) :
        print("Property Sales price: ", amount)

    @abstractmethod
    def payment(self,amount):
        pass

class Property1(properties):
    def payment(self,amount):
        print('Property purchase price of {} was $50k under asking price'.format(amount))

obj = Property1()
obj.salesPrice("$400")
obj.payment("$350")
        





