from math import sqrt

def prime_factors(number):
    result = []
    power = 0
    while number % 2 == 0:
        power = power + 1
        number = number / 2
    if power:
        result.append([2, power])
    for i in range(3,int(sqrt(number))+1,2):
        power = 0
        while (number % i == 0):
            power = power + 1
            number = number / i
        if power:
            result.append([i, power])
    if number > 2:
      result.append([round(number), 1])
    return result