class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name+"села")
    def roll_over(self):
        print(self.name+"перекатилась")

my_dog = Dog("willie ", 6)
my_dog.sit()
my_dog.roll_over()
my_dog = Dog("lucy ", 3)
my_dog.sit()
my_dog.roll_over()