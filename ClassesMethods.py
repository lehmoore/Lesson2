# A class is a "blueprint" for creating objects.

# Creating a class

# class Dog:
#     animal_kind = "Canine"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     Adding method
    # def bark (self):
    #     return("Woof")
    # def eat(self):
    #     return("Yum")
    # def run(self):
    #     return("Pant")
#
# Instantiation of objects

# Dog1 = Dog("Callie", 7)
# Dog2 = Dog("Phlox", 6)
# Dog3 = Dog("Skip", 14)
#
# print(type(Dog1))
#
# print(Dog1.bark())
# print(Dog1.animal_kind)
# print(Dog1.eat())
# print(Dog2.eat())
# print(Dog1.run())
# print(Dog2.run())
# print(Dog1.name)
# print(Dog2.name)

# print("{} is {} years old".format(Dog1.name, Dog1.age))

# print("The oldest dog is {} years old".format(max(Dog1.age, Dog2.age, Dog3.age)))
# print("The youngest dog is {} years old".format(min(Dog1.age, Dog2.age, Dog3.age)))

# name = [Dog1.name, Dog2.name, Dog3.name]



# print("What year is it?")
# year = int(input())
#
# def leap(num):
#     for m in range (1,10000000000)
#
# if year % 4 == 0:
#     print(year, "is a leap year!")
# else:
#     print(year, "is not a leap year!")


# print("Pick a number:")
# Number = int(input())
#
# def fizzbuzz(num):
#     for m in range(1, num+1):
#         if m == 0:
#             print(l)
#         elif m % 3 == 0 and m % 5 == 0:
#             print("FizzBuzz")
#         elif m % 5 == 0:
#             print("Fizz")
#         elif m % 3 == 0:
#             print("Buzz")
#         else:
#             print(m)
#
# fizzbuzz(Number)

# print("What year would you like to check?")
# year = int(input())
#
# def leap():
#     if year % 4 != 0:
#         print("It is not a leap year!")
#     elif year % 100 != 0:
#         print("It is a leap year!")
#     elif year % 400 != 0:
#         print("It is a common year!")
#     else:
#         print("It is a leap year!")
# leap()

# BELOW CODE DOESN'T WORK THE WAY IT SHOULD AND I DON'T KNOW WHY

# list1 = ['abc', 'xyz', 'aba', '1221']
#
# def firstLast(list1):
#     count = 0
#     for m in list1:
#         if m[0] == m[-1]:
#             count += 1
#     return count