print("Любите ли вы котиков?")
answer1 = input()
print("Любите ли вы мышей?")
answer2 = input()
if answer1 == "да" and answer2 == "да":
    print("Поздравляю, вы любите животных!")
elif answer1 == "нет" and answer2 == "нет":
    print("Вы жестокий человек!")
elif answer1 == "да" and answer2 == "нет":
    print("Вы любитель кошек!")
elif answer1 == "нет" and answer2 == "да":
    print("Вы любитель мышей!")
else:
    print("Вам нужно было написать да или нет.")