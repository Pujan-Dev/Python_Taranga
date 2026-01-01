class Users:
    role = "Admin"
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"User Name is {self.name} and Role is {self.role}"
    def __repr__(self):
        return f"Users('{self.name}')"

u1 = Users("Alice")
# print(u1)
# print(u1.role)
# print(u1.name)
print(repr(u1))