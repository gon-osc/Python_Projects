
class Company:
    def __init__(self, name, proj):
        self.name = name      
        self._proj = proj


class Emp(Company):
    def __init__(self, eName, sal, cName, proj):
        Company.__init__(self, cName, proj)
        self.name = eName   
        self.__sal = sal    
    

    def show_sal(self):
        print("The yearly salary of ",self.name," is ",self.__sal,)


c = Company("Apple", "Iphone12")

e = Emp("Bob", '$75,000', c.name, c._proj)

print("Welcome to ", c.name)
print(e.name,"is working on the",e._proj)


e.show_sal()
