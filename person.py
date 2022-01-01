class Person:
    def __init__ (self,name,age):
        print("person object is created")
        self.name = name
        self.age = age
    def money(self):
        print("YOU GOT $1000")
        

lakshya = Person("nisha",28)
devansh = Person("devansh",15)

print(lakshya.age)
print(devansh.name,devansh.age)

lakshya.money() 