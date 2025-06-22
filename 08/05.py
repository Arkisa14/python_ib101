word = input()
while True:
    new = input()
    if new[0] != word[-1]:
        break
    word = new
print(new)