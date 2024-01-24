class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display_details(self):
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")


if __name__ == "__main__":
   
    student1 = Student("Alice Johnson", "S001")
    student2 = Student("Bob Smith", "S002")

    
    print("Student Details:")
    student1.display_details()
    print("\n")
    student2.display_details()

        
        
