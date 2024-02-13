# Data Type
number = 45 # int
num = 56.78 # float
greeting = "Heello there" # str
isPythonInteresting = True # bool

# Variable storing multiple values
languages = ["python","php","javascript"] #
fruits = ("apple","banana","orange") # Tuple
countries = {"China","bangladesh","USA"} # set
# Dictionary
details = {
    "firstname" : "Collins",
    "age" : 19,
    "course" : "MIT",
    "nationality" : "Arizona",
}
print(details["course"])
print(details["nationality"])
print(details)
print(number)
print(greeting)
print(countries)
print(isPythonInteresting)

# Determining the data type
print(type(details))
print(type(countries))

# Tye casting - converting one data type to another
print(float(number))
print(int(num))
