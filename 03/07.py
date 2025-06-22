num = float(input())
if abs(num) < 1e-6:
    print(1000000)
else:
    print(1 / num)