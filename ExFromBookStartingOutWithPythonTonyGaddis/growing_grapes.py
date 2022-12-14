"""Владелец виноградника высаживает несколько новых гряд
винограда, и ему нужно знать, сколько виноградных лоз следует посадить на каждой 
гряде. Измерив длину будущей гряды, он определил, что для расчета количества виноградных лоз, 
которые поместятся на гряду вместе с концевыми опорами, которые должны быть установлены в конце каждой гряды,
 он может применить приведенную ниже 
формулу:  V = (R - 2E)/S,
где V — количество виноградных лоз, которые поместятся на гряде; R — длина гряды 
в метрах; Е — размер пространства в метрах, занимаемого концевыми опорами; S — 
расстояние между виноградными лозами в метрах.
Напишите программу, которая для владельца виноградника выполняет расчеты. Данная 
программа должна попросить пользователя ввести:
• длину гряды в метрах;
• пространство, занимаемое концевой опорой в метрах;
• расстояние между виноградными лозами в метрах.
После того как входные данные будут введены, программа должна рассчитать и показать количество виноградных лоз,
 которые поместятся на гряде."""


def get_vines_count(ridge_length, end_support, between_vines):
    return round((ridge_length - 2 * end_support) / between_vines)


r = float(input('Введите длину гряды в метрах:'))
e = float(input('Введите пространство для концевых опор в метрах:'))
s = float(input('Введите расстояние между лозами в метрах:'))

v = get_vines_count(r, e, s)
print(f'Количество виноградных лоз на гряде = {v}')

