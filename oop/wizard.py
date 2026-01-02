# Define the Wizard class
class Wizard:
    
    def __init__(self, name):
        
        if not name:
            raise ValueError("Name cannot be empty")
        
        self.name = name
        ...

# Define the Student class that inherits from Wizard
class Student(Wizard):
    
    def __init__(self, name, house):
        
        super().__init__(name)
        self.name = name
        self.house = house
        ...


# Define the Professor class that inherits from Wizard
class Professor(Wizard):
    
    def __init__(self, name, subject):
        
        super().__init__(name)
        self.name = name
        self.subject = subject
        ...

# Create instances of the Wizard, Student, and Professor classes
wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")