# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
from itertools import groupby


def rle_encode(data):  # Кодирование длин серий
    result = ''
    prev = ''
    count = 1
    for ch in data:
        if ch != prev:
            if prev:
                result += str(count) + prev
            count = 1
            prev = ch
        else:
            count += 1
    else:
        result += str(count) + prev
        return result


def rle_decode(data):
    result = ''
    count = 0
    for ch in data:
        if ch.isdigit():
            count = int(ch)
        else:
            result += ch * count
            count = 0
    return result


# считываем строку с файла, убирая лишнее и кодируем
with open('input_data.txt', 'r') as i:
    text = i.read().replace('\n', ' ').replace('\r', '')
    encode_text = rle_encode(text)
# записываем кодированный текст в новый файл
with open('encode_data.txt', 'w') as e:
    e.write(encode_text)
# записываем декодированный текст в новый файл
with open('decode_data.txt', 'w') as d:
    decode_text = rle_decode(encode_text)
    d.write(decode_text)


