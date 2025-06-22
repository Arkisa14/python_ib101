a = int(input())
b = int(input())
if a >= b:
    print("Неправильно. a должно быть меньше b")
for i in range(a, b+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)