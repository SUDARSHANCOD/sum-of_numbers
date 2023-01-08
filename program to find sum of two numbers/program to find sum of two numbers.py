#sum of two numbers by using function definition
def addnumbers(a,b):
    return a+b
print('sum of two digits: %d'%addnumbers(1,2))

#sum of two numbers by using basic arthematic operation
a = 1
b = 2
print('sum of two numbers: %d'%(a+b))

#sum of two numbers by using class instance method
class digitsum:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sumofdigits(self):
        return self.a + self.b
digits = digitsum(1,2)
print('sum of two digits: %d'%(digits.sumofdigits()))

#sum of two numbers by using class method
class digitsum:
    @classmethod
    def sumofdigits(cls,a,b):
        return a+b
print("sum of two numbers: %d"%(digitsum.sumofdigits(1,2)))

#sum of two digits by taking list of digits
def sumofdigits(digits):
    total = 0
    for digit in digits:
        total += digit
    return total
print("sum of two numbers: %d"%(sumofdigits([1,2])))