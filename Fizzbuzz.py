# # BARE BONES FIZZBUZZ
#
# for m in range (1, 100+1):
#     if m % 3 == 0 and m % 5 == 0:
#         print("FizzBuzz")
#     elif m % 5 == 0:
#         print("Fizz")
#     elif m % 3 == 0:
#         print("Buzz")
#     else:
#         print(m)

# # INPUT RANGE WITHOUT FUNCTIONS
#
# print("Pick a number:")
# Number = int(input())
#
# for m in range (1, Number + 1):
#     if m % 3 == 0 and m % 5 == 0:
#         print("Fizzbuzz")
#     elif m % 5 == 0:
#         print("Fizz")
#     elif m % 3 == 0:
#         print("Buzz")
#     else:
#         print(m)

# # INPUT RETURNS INPUT SINGLE VALUE
#
# print("Pick a number:")
# Number = int(input())
#
# def fizzbuzz(m):
#     if m % 3 == 0 and m % 5 == 0:
#         print("FizzBuzz")
#     elif m % 5 == 0:
#         print("Fizz")
#     elif m % 3 == 0:
#         print("Buzz")
#     else:
#         print(m)
#
# fizzbuzz(Number)

# # INPUT RETURNS INPUT RANGE
#
print("Pick a number:")
Number = int(input())

def fizzbuzz(m):
    for m in range(1, m + 1):
        if m % 3 == 0 and m % 5 == 0:
            print("FizzBuzz")
        elif m % 5 == 0:
            print("Fizz")
        elif m % 3 == 0:
            print("Buzz")
        else:
            print(m)

fizzbuzz(Number)