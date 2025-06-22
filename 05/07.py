n = int(input())
t = 0
for i in range(1, n + 1):
    if n % i == 0:
        t += 1
        print(i, end=" ")
if t == 2:
    print("\nПростое")
else:
    print("\nНет")