"""Напишите программу, удаляющую из текста все слова, содержащие ""абв""."""

text = input("Введите текст через пробел:\n")
FIND_TEXT = "абв"
res_text = [i for i in text.split() if FIND_TEXT not in i]
print(f'Результат: {" ".join(res_text)}')
