print("Количество строк: ")
strings = int(input())
cat_found = False
for i in range(strings):
    s = input()
    if "Кот" in s or "кот" in s:
        cat_found = True
        break
if cat_found == True:
    print("МЯУ")
else:
    print("НЕТ")