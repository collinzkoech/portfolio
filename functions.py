# Inbuilt functions
number = max(89,70,20,44,12)
print(number)

x = min(76, 93, 33, 3)
print(x)

z  = pow(2,3)
print(z)

# User-defined functions
def name():
    print("Collins")

name() # Calling a function


def student():
    name = "Collins"
    age = 18
    course = "MIT"
    print(name, age, course)
student()

#  Parameters/Variables and arquments/varues

def student(name, age, course):
    print(name, age, course)
student("Grace", 17,"MIT")
student("Collins", 18,"Cybersefcurity")
student("Jonte", 17,"Accountant")
student("Vitalis", 19,"Engineering")
student("Joan", 17,"Cybersecurity")

# create  a user defined function called employ. it should display
# details of five employees.parameters are
# fullname, age, gender, position, salary
def employ(fullname, age, gender, position, salary):
    print(fullname, age, gender, position, salary)
employ("Grace Achieng", 20,"female", "secretary","Kes. 15000")
employ("Victor Serem", 23,"male", "Accountant","Kes. 18000")
employ("Ann Karimi", 24,"female", "Receptionist","Kes. 16000")
employ("Dennis Krisner", 28,"male", "CEO","Kes. 50000")
employ("Andrew Patel", 30,"male", "Engineer","Kes. 30000")

