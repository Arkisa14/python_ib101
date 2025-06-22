line_number = 0
found = False
first_cat_line = 0
while True:
    s = input()
    line_number += 1
    if not found:
        if "Кот" in s or "кот" in s:
            found = True
            first_cat_line = line_number
            break
    if s == "СТОП":
        break
print(first_cat_line if found else -1)