# FizzBuzz program (for)
for number in range(1, 101):

    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# FizzBuzz program (while)
count = 1

while count < 101:
    if count % 15 == 0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)
    count += 1

# FizzBuzz program (break)
count = 1

while True:
    if count > 50:
        break
    if count % 15 == 0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)
    count += 1

# FizzBuzz program (continue)
count = 0
while count < 30:
    count += 1
    if count % 2 == 0:
        continue
    if count % 15 == 0:
            print("FizzBuzz")
    elif count % 3 == 0:
            print("Fizz")
    elif count % 5 == 0:
            print("Buzz")
    else:
        print(count)
