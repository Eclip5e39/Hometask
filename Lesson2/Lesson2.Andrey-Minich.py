# Написать программу, которая
# - Запрашивает у пользователя имя и возраст;
# - Проверяет минимальный возраст 14;
# - Проверяет, что имя введено и минимальное количество символов в имени — 3;
# - Проверяет возраст на отрицательное число или 0;
# - Проверяет имя на пустоту;
# * Проверяет, что возраст возраст 16-17 лет и нужно не забыть получить первый паспорт; возраст 25-26 лет и нужно заменить паспорт; возраст 45-46 лет и нужно второй раз заменить паспорт;
# - Выводит либо текст с ошибкой (по каждому условию разный текст ошибки), либо приветствие пользователя с его именем (с заглавной буквы), указанием возраста и *советом получить/заменить паспорт (если совет актуален).
# * Совет с паспортом выводить только в том случае, если отображается приветствие.

# Ограничения:
# - только один раз можно использовать print

name = str(input('Введите имя\n'))
age = int(input('Введите свой возраст:'))
if len(name) < 3:
    len_name = 'Имя не должно быть пустым и не меньше 3-х символов!'
else:
    len_name = ''
if 14 > age > 0:
    age_14 = 'Ошибка:\nМинимальный возраст 14 лет!'
else:
    age_14 = ''
if age <= 0:
    age_print = 'Возраст не может быть меньше, либо равен нулю!'
else:
    age_print = ''
if age == 16 or age == 17:
    passport = 'Нужно не забыть получить первый паспорт'
elif age == 25 or age == 26:
    passport = 'Нужно заменить паспорт'
elif age == 45 or age == 46:
    passport = 'Нужно второй раз заменить паспорт'
else:
    passport = ''
print(f'Приветствую {name.capitalize()}! {len_name}\nВаш возраст {age}! {age_14}{age_print}\n{passport}')