print("Куда едем в июле?")
city1 = input()
print("Куда едем в августе?")
city2 = input()
if city1 == "Тула" and city2 == "Пенза" or city1==city2:
    print("Не-а")
elif city1 == "Тула" or city2 == "Пенза":
    print("Поехали!")
else:
    print("Так не пойдёт")