# WHILE LOOP

# With the while loop we can execute a set of statements as long as a condition is true

# i = 1
# while i < 6:
#     print(i)
#     i += 1
#
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1
#
# List_2 = [25, 30, 56, 78, 86, 45]
# # for k in List_2:
# #     if (k % 2) == 0:
# #         print(k, "is even.")
# #     else:
# #         print(k, "is odd.")
#
# print("There are", sum(1 for i in List_2 if i%2 == 0), "even numbers in the list.")
# print("There are", sum(1 for i in List_2 if i%2 != 0), "odd numbers in the list.")

# for num in range(1,50):
#     string = ""
#     if num % 3 == 0:
#         string = string + "Fizz"
#     if num % 5 == 0:
#         string = string + "Buzz"
#     if num % 5 != 0 and num % 3 != 0:
#         string = string + str(num)
#     print(string)

# for num in range(1, 51):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# num = int(input("Enter a number:"))
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)

# print("Enter a number:")
# input_range = int(input())
#
# print("Enter a number:")
# target = int(input())
#
# if target % 3 == 0 and target % 5 == 0:
#     print("FizzBuzz")
# elif target % 3 == 0:
#     print("Fizz")
# elif target % 5 == 0:
#     print("Buzz")
# else:
#     print(target)

print("Enter a number:")
input_range = int(input())

for num in range(1, input_range):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)