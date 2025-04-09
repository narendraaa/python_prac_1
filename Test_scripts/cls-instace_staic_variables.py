class A:
    # l1 = ['a','b','c']  # class variable
    l1 = []
    def __init__(self,l2):
        self.l2 = l2  # instance variable
    def show(self): #instance method
        dict = {}
        for i in range(len(A.l1)):
            dict[A.l1[i]] = self.l2[i]
        print(dict)
    @classmethod
    def create_dict(cls,l3):
        cls.l3= l3
        d2 = {}
        for i in range(len(A.l1)):
            d2[A.l1[i]] = cls.l3[i]
        print(d2)

    @staticmethod
    def greet(l4):
        d3 = {}
        for i in range(len(A.l1)):
            d3[A.l1[i]] = l4[i]
        print(d3)







A.l1 = ['x','y','z'] # updaing calss variable values
l2 = [1,2,3]
l3 = [5,6,7]
l4 = [8,9,3]
obj = A(l2)
obj.show()
A.create_dict(l3)
A.greet(l4)





