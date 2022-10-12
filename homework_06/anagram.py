"""
Завершите функцию, чтобы вернуть значение true,
если два приведенных аргумента являются анаграммами друг друга;
в противном случае верните значение false.
"""


# Было
def is_anagram(test, original):
    test = list(test.lower())
    original = list(original.lower())
    test.sort()
    original.sort()

    pos = 0
    match = True

    if len(test) != len(original):
        return False
    else:
        while pos < len(test) and match:
            if test[pos] == original[pos]:
                pos += 1
            else:
                match = False

    return match


# Используя lambda и sorted
is_anagram = lambda t, o: sorted(t.lower()) == sorted(o.lower())
