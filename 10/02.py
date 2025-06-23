n = int(input())
lines = [input() for i in range(n)]
pattern = input()
for line in lines:
    if pattern in line:
        print(line)