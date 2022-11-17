"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
ENC_WORDS = []
for item in ['разработка', 'администрирование', 'protocol', 'standard']:
    ENC_WORDS.append(item.encode())
    print(item.encode())
for item in ENC_WORDS:
    print(item.decode())