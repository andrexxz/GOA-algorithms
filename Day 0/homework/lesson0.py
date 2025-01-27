#1)
def count_divisibles(a, b, c):
    if c == 0:
        return 0

    start, end = min(a, b), max(a, b)
    first_divisible = start + (c - start % c) if start % c != 0 else start
    last_divisible = end - end % c

    if first_divisible > end:
        return 0

    return ((last_divisible - first_divisible) // c) + 1
#2)
def to_decimal(number, base):
    decimal = 0
    power = 0
    for digit in reversed(str(number)):
        decimal += int(digit) * (base ** power)
        power += 1
    return decimal

def from_decimal(decimal, base):
    result = ""
    while decimal > 0:
        result = str(decimal % base) + result
        decimal //= base
    return result or "0"

def convert_base(number, from_base, to_base):
    decimal_number = to_decimal(number, from_base)
    return from_decimal(decimal_number, to_base)
#3)
def find_max(array):
    maximum = array[0]
    for num in array:
        if num > maximum:
            maximum = num
    return maximum
