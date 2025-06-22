count = 0
total = 0
result = None
while True:
    s = input()
    if s == '0':
        break
    num = int(s)
    count += 1
    total += num
    if total == 10 and result is None:
        result = count
print(result)