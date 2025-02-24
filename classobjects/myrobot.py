class Robot_Dog:
    def __init__(self, var_name, var_breed):
        self.name = var_name
        self.breed = var_breed

    def bark(self):
        print("Woof! Woof!")

#MAIN
my_dog = Robot_Dog("Tiny", "American Bulldog")

print(my_dog.name)
print(my_dog.breed)
my_dog.bark()