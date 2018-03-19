from math import sqrt


def is_square(n):
    return not (n**(1/2) % 1) > 0 if n > 1 else False


def is_square_alt(n):
    if n > 1 and sqrt(n).is_integer():
            return True
    return False


print(is_square_alt(25))
