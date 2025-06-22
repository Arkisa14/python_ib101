n = int(input())
fact = 1
if n == 0:
    print("1")
elif n < 0:
    print("Нужно положительное число.")
elif n > 0:
    for i in range(1, n + 1):
        fact *= i
    print(fact)

    