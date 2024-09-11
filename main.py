# create class
class Parrot:

    #class attribute
    species="bird"

    #instance attribute
    def __init__(self,name,age):
        self.name=name
        self.age=age

# the Parrot Class
Green=Parrot("Green",10)
hello=Parrot("hello",13)

# Acess the class attributes
print("Green is a {}".format(Green.name, Green.age))
print("hello is also a {}".format(hello.name, hello.age))
                     
        