# def main():
    
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------>

# def main():
    
#     name, house = get_student()
#     print(f"{name} from {house}")

# def get_student():
    
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house

# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------>

# def main():

      # Get the name and house from the user using the get_student function to a tuple containing the name and house
#     student = get_student()
      # Print the name and house of the student by accessing the first and second elements of the tuple respectively
#     print(f"{student[0]} from {student[1]}")

# def get_student():

#     name = input("Name: ")
#     house = input("House: ")
      # return a tuple
#     return (name, house) 

# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------>

# def main():

      # Get the name and house from the user using the get_student function to a list containing the name and house
#     student = get_student()
    
    # If the name is Padma, change her house to Ravenclaw. We can do this in list but but not in a tuple because tuples are immutable and lists are mutable.
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    
      # Print the name and house of the student by accessing the first and second elements of the list respectively
#     print(f"{student[0]} from {student[1]}")

# def get_student():
    
#     name = input("Name: ")
#     house = input("House: ")
#     # return a list
#     return [name, house]

# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------>

# def main():
    
      # Get the name and house from the user using the get_student function to a dictionary containing the name and house
#     student = get_student()
    
      # If the name is Padma, change her house to Ravenclaw. We can do this in dictionary also.
#     if student['name'] == "Padma":
#         student['house'] = "Ravenclaw"
    
      # Print the name and house of the student by accessing the keys of the dictionary respectively
#     print(f"{student['name']} from {student['house']}")

# def get_student():
    
      # Get the name and house from the user in the format of a dictionary
#     student = {"name": input("Name: "), "house": input("House: ")}
      # student = {}
      # student["name"] = input("Name: ")
      # student["house"] = input("House: ")
      # name = input("Name: ")
      # house = input("House: ")
      # return a dictionary
      # return {"name": name, "house": house}
#     return student

# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------>

# Define a Student class with attributes name and house
# class Student:
#     ...

# def main():
    
      # Get the name and house from the user using the get_student function to a Student object
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
    
      # Get the name and house from the user in the format of a Student object
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
      # return a Student object
#     return student

# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------>

# Define a Student class with attributes name and house
# class Student:
    
      # Initialize the attributes name and house of the Student class
#     def __init__(self, name, house): 
        
#         self.name = name
#         self.house = house
    
      # Implementing a string representation of the Student object
#     def __str__(self): 
#         return f"{self.name} from {self.house}"
    
      # Getter method for the name attribute
#     @property
#     def name(self):
#         return self._name
    
      # Setter method for the name attribute
#     @name.setter
#     def name(self, name):
    
          # Check if the name and house are not empty strings and raise a ValueError if they are
#         if not name:
#             raise ValueError("Name cannot be empty")
        
#         self._name = name
    
      # Getter method for the house attribute
#     @property
#     def house(self):
#         return self._house
    
      # Setter method for the house attribute
#     @house.setter
#     def house(self, house):
        
          # Check if the house is not empty and raise a ValueError if it is
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("House cannot be empty")
        
#         self._house = house

# def main():
    
#     # Get the name and house from the user using the get_student function to a Student object
#     student = get_student()
#     # print(f"{student.name} from {student.house}")
#     print(student)

# def get_student():
    
#     name = input("Name: ")
#     house = input("House: ")
#     # Create a Student object with the given name and house and return it
#     return Student(name, house)

# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------>

# Define a Student class with attributes name and house
# class Student:
    
    # Initialize the attributes name and house of the Student class
    # def __init__(self, name, house): 
        
    #     self.name = name
    #     self.house = house
    
    # Implementing a string representation of the Student object
    # def __str__(self): 
    #     return f"{self.name} from {self.house}"
    
    # @classmethod
    # def get(cls): 
        
    #     name = input("Name: ")
    #     house = input("House: ")
    #     return cls(name, house)

# def main():
    
    # Get the name and house from the user using the get_student function to a Student object
    # student = Student.get()
    # print(f"{student.name} from {student.house}")
#     print(student)

# if __name__ == "__main__":
#     main()