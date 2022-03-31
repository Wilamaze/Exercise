""" Python file for the exercise assignment"""\
    
class Person:
    """A person within our group
    
    Attributes:
    number (int): The person's number we are assigning them to.
    name (str): The person's name within our group.
    """
    
    def __init__(self, number, name):
        self.number = number
        self.name = name
    
    def __str__(self):
        return "Group Member Number " + str(self.number) + \
            " and their name is " + self.name + "!"
    
# Group Members putting their number and name here.
orlando = Person(1, "Orlando Aguilar")
print(orlando)
yaseen = Person(2, "Yaseen Muhammad")
print(yaseen)
daniel = Person(3, "Daniel Kolawole")
print(daniel)