print('Задача 10. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.
 
# Напишите программу, 
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
 
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

# Подсказка: используйте бинарный поиск, а не конкатенацию.
lower_number = 1
upper_number = 100
N = (lower_number + upper_number) // 2
counts = 0
while True:
  print('Твое число равно, меньше или больше, чем число ', N, '?', sep='')
  counts += 1
  answer = input('1 - равно, 2 - больше, 3 - меньше: ')
  if answer == '1':
    print('Я угадал. Твое число -', N)
    break
  elif answer == '2':
    lower_number = N + 1
    N = (lower_number + upper_number) // 2
  else:
    upper_number = N - 1
    N = (lower_number + upper_number) // 2
print('Количество попыток угадать:', counts)