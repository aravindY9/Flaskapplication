



class car:

    def __init__(self, a,b):
        print ("self is :", self)
        self.a  = a
        self.b = b
        self.name = "vamsi"

    def summ(self, a, b):
        return a + b

    def three_sum(self, f):
        return  self.a + self.b + f

    def hello(self):
        return self.name


obj1 = car(10,20)



print (dir(obj1))









