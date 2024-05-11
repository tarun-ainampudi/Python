class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")
        super().method()

class C(A):
    def method(self):
        print("C method")
        super().method()

class D(B, C):
    pass

# Creating an instance of D and calling method
instance_d = D()
instance_d.method()

    

      
    