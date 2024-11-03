class Employee:
    raise_amt = 1.04

    def_init_(self, first, last, pay): # type: ignore
        self.first = first
        self.last = last
        self.email = frist + '.' + '@email.com'
        self.pay = pay
    

    def fullname(self):
        return '{} {}' .format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    pass


dev_1 = Developer('Corvey','Sulafer',5000)
dev_2 = Developer('Test','Employee',6000)


print(dev_1.email)
print(dev_2.email)
print(dev_1.fullname())
print(dev_2.fullname())
