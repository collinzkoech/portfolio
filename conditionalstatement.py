temperature = 13

if temperature > 25 :
    print("It is hot ")
else:
    print("It is cold")

# A program that the largest numbers among three numbers
num1 = 40
num2 = 49
num3 = 28
if num1 > num2 and num1 > num3:
    print(num1,"is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2,"is the largest number")
else:
    print(num3, "is the largest number")
if num1 < num2 and num1 < num3:
    print(num1,"is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2,"is the smallest number")
else:
    print(num3, "is the smallest number")

# Program that checks whether a number is even or odd
number = 43
if number % 2 == 0:
    print(number , "is an even number")
else:
    print(number, "is an odd number")

# Program that checks whether a number is a prime number or not
num = 20
for i in range(2,num):
    if num % i == 0:
        print(num, " is not a prime number")
        break
else:
    print(num, "is a prime number")