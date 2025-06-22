low = 1
high = 1000
for i in range(10):
    mid = (low + high) // 2
    print(mid)
    response = input()
    if response == '=':
        break
    elif response == '>':
        low = mid + 1
    elif response == '<':
        high = mid - 1