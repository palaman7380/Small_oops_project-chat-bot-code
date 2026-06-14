class fraction:

    def __init__(self,x,y):
        self.num = x
        self.den = y

    def __str__(self,):
        return '{}/{}'.format(self.num, self.den) # self.num= x and other stored = y
    
    def __add__(self,other):
        Add1 =self.num * other.den + other.num * self.den
        Add2 = self.den * other.den

        return '{}/{}'.format(Add1,Add2)
    
    def __sub__(self,other):
        sub1 =self.num * other.den - other.num * self.den
        sub2 = self.den * other.den

        return '{}/{}'.format(sub1,sub2)
    
    def __mul__(self,other):
        new_num = self.num*other.num
        new_den = self.den*other.den

        return '{}/{}'.format(new_num,new_den)

    def __truediv__(self,other):
        new_num = self.num*other.den
        new_den = self.den*other.num

        return '{}/{}'.format(new_num,new_den)

    def convert_to_decimal(self):
        return self.num/self.den

    





