# Задание 1 ------------------------------------------------------------------
name = input('Ваше имя')  # Задание 1
print(name)
# Задание 2 ------------------------------------------------------------------
age = input('Ваш возраст')  # Задание 2
print('Меня зовут', name, ', мне', age, 'лет.')
# Задание 3 ------------------------------------------------------------------
nameX5 = input('Ваше имя')  # Задание 3
print("Ваше имя 5 раз: ")
for i in range(5):
    print(nameX5 + "")

# Задание 4 ------------------------------------------------------------------
askName = str(input('Как вас зовут?'))  # Задание 4
askAge = int(input('Сколько вам лет?'))
if askAge <= 18:
    print('Здравствуйте', askName, ', вы ещё слишком малы.')
else:
    print('Здравствуйте', askName, ', вы уже слишком стары.')

# Задание 5 ------------------------------------------------------------------
userAge = int(input('Сколько вам лет?'))  # Задание 5
if userAge <= 18:
    print("Мне кажется вы любите поесть песок.")
else:
    print("Мне кажется из вас уже сыпется песок.")

# Задание 6 ------------------------------------------------------------------
userName = input('Введите имя пользователя')  # Задание 6
print('Имя пользователя без первого и последнего символа',  userName[1:-1],
      ', \nИмя пользователя задом наперёд',userName[::-1],
      ", \nпоследние 3 символа вашего имени пользователя", userName[-3:],
      ', \nпервые 5 символов вашего имени пользователя', userName[:5])

# Задание 7 ------------------------------------------------------------------
userAge = input('Сколько вам лет?')  # Задание 7
userName = input('Введите имя пользователя')
sumAge = int(userAge[0]) + int(userAge[1])
mulAge = int(userAge[0]) * int(userAge[1])
print('Длина вашего имени пользователя', len(userName),
      ', \nсумма чисел вашего возраста', sumAge,
      ', \nпроизведение чисел вашего возраста', mulAge)

# Задание 8 ------------------------------------------------------------------
userNameReg = str(input('Введите имя пользователя '))  # Задание 8
print("Имя пользователя в верхнем регистре: ", userNameReg.upper(),
      "\nИмя пользователя в нижнем регистре: ",   userNameReg.lower(),
      "\nИмя пользователя с первой заглавной: ", userNameReg.capitalize(),
      "\nИмя пользователя с первой строчной: ", userNameReg.lower())

# Задание 9 Имя ------------------------------------------------------------------
while True:  # Задание 9 Имя
    userNameStr = input("Введите ваше имя: ")
    if userNameStr.isspace():
        print("Пиши имя без пробелов! Попробуй еще раз: ")
        break
    elif userNameStr.isdigit():
        print("Пиши строку! Попробуй еще раз: ")
        break
    else:
        print("Молодец!")
    break

# Задание 9 Возраст ------------------------------------------------------------------
while True:  # Задание 9 Возраст
    try:
        userAgeInt = int(input("Введите ваш возраст: "))
        if 0 <= userAgeInt <= 150:
            print('Молодец!')
            break
        else:
            raise ValueError
    except ValueError:
        print("Вы ввели не число или число не входит в диапазаон [0, 150]."
              " \nПопробуйте снова: ")

# Задание 10 ------------------------------------------------------------------
while True:  # Задание 10
    try:
        prim = int(input("Сколько будет : 52 * 48? "))  # Ответ : 2496
        if prim == 2496:
            print('Верно!')
            break
        else:
            raise ValueError
    except ValueError:
        print("Неверно! Попробуйте заново: ")
exit(0)
