# square = lambda x : x*x 
# print(square(3))
# why is X defined?
# X= 10
# def demo ( ):
#     x= 5
#     print("inside",x)
# print("outside",x)
# demo()

class User:
    role="admin"
    def __init__(self,name):
        self.name= name

    def display(self):
        print(self.name)

u1 = User("Pujan")
u1.display()

