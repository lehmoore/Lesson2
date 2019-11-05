for m in range (1, 50 + 1):
    if m % 5 == 0 and m % 3 == 0:
        print("Fizzbuzz")
    elif m % 5 == 0:
        print("Fizz")
    elif m % 3 == 0:
        print("Buzz")
    else:
        print(m)

print("Pick a number:")
Number = int(input())

for m in range (1, Number + 1):
    if m % 5 == 0 and m % 3 == 0:
        print("Fizzbuzz")
    elif m % 5 == 0:
        print("Fizz")
    elif m % 3 == 0:
        print("Buzz")
    else:
        print(m)

print("Pick a number:")
Number = int(input())

def fizzbuzz(m):
    for m in range (1, m + 1):
        if m % 5 == 0 and m % 3 == 0:
            print("Fizzbuzz")
        elif m % 5 == 0:
            print("Fizz")
        elif m % 3 == 0:
            print("Buzz")
        else:
            print(m)

fizzbuzz(Number)

print("Pick a number:")
Number = int(input())

def fizzbuzz(m):
    if m % 5 == 0 and m % 3 == 0:
        print("Fizzbuzz")
    elif m % 5 == 0:
        print("Fizz")
    elif m % 3 == 0:
        print("Buzz")
    else:
        print(m)

fizzbuzz(Number)
