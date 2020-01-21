def convert(number):
    sounds = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }
    result = ''
    for key, value in sounds.items():
        if number % key == 0:
            result += value
    if result == '':
        return str(number)
    return result
