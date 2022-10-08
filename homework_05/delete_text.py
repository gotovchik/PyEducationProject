# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст через пробел:\n")
find_text = "абв"
res_text = [i for i in text.split() if find_text not in i]
print(f'Результат: {" ".join(res_text)}')
