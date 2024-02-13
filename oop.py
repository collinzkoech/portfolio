class person:
    def __init__(self,firstname,age,gender):
        self.firstname = firstname
        self.age = age
        self.gender = gender
    def details(self):
        print(self.firstname,"is studying")
teacher = person("John",30,"male")
accountant = person("Jean",28,"female")
doctor = person("james",34,"male")
print(teacher.firstname,teacher.age,teacher.gender)
print(accountant.firstname,accountant.age,accountant.gender)
print(doctor.firstname,doctor.age,doctor.gender)