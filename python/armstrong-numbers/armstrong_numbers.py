def split(n):
    s = str(n)
    return [s[i] for i in range(0, len(s))]

def is_armstrong_number(number):
    result = 0
    splited_number = split(number)
    for i in splited_number:
        result = result + (int(i) ** len(splited_number))
    return number == result
