def find_factors(number):
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    return factors

def aliquot_sum(factors):
    result = 0
    for i in factors:
        result += i
    return result

def classify(number):
    if number < 1:
        raise ValueError("Number must be more than 0 and be natural numbers, your number was {number}.")

    aliquot = aliquot_sum(find_factors(number))

    try:
        if number == aliquot:
            return "perfect"
        elif number < aliquot:
            return "abundant"
        else:
            return "deficient"
    except:
        raise Exception("No classification found.")