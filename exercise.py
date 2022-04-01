""" Python file for the exercise assignment"""\
    
class Person:
    """A person within our group
    
    Attributes:
    number (int): The person's number we are assigning them to.
    name (str): The person's name within our group.
    """
    
    def __init__(self, number, name):
        """Initializing class instance and attributes.

        Args:
            number (int): The number of the group member
            name (str): The name of the group member.
        """
        self.number = number
        self.name = name
    
    def __str__(self):
        """The method that will print out the message

        Returns:
            String: Returns the number and the name of the group member
        """
        return "Group Member Number " + str(self.number) + \
            " and their name is " + self.name + "!"
    
# Group Members putting their number and name here.
orlando = Person(1, "Orlando Aguilar")
print(orlando)
yaseen = Person(2, "Yaseen Muhammad")
print(yaseen)
daniel = Person(3, "Daniel Kolawole")
print(daniel)
mohamed = Person(4, "Mohamed Barrie")
print(mohamed)
emerson = Person(5, "Emerson Kelley")
print(emerson)