# This program adds fractions together
# Author: Yiping (Allison)
# December 2017

def is_int(string_int: str) -> bool:
    """
    gets string from is_a_fraction and checks if inside para are ints
    :param string_int:
    :return:
    """
    string_int = string_int.strip()
    if len(string_int) == 0:
        return False
    elif string_int.isdigit():
        return True
    elif string_int[0] == '-' and string_int[1:].isdigit():
        return True
    else:
        return False

def is_a_fraction(fraction: str) -> bool:
    """
    checks valid inputs of fractions
    :param fraction:
    :return:
    """
    if len(fraction) == 0:  # pre-checks
        return False
    elif len(fraction) == 1 and fraction == '0':
        return False
    elif is_int(fraction):  # if value is an int
        return True
    elif fraction.count('/') > 1:
        return False

    if '/' in fraction:  # splitting fraction for more validation
        fract_split = fraction.split('/')
        numerator, denominator = fract_split
        numerator = numerator.strip()
        denominator = denominator.strip()
        if denominator[0] == '-':
            return False
        elif denominator == '0':
            return False
        elif (numerator[0] == '-' and is_int(numerator[1:]) and is_int(denominator))\
                or (is_int(numerator) and is_int(denominator)):  # if the numerator and denom is int
            return True

def split_fraction(fraction: str) -> tuple:
    """
    gets validated fractions in string form
    turns the string into individual ints
    then returns ints in tuple form
    :param fraction:
    :return:
    """
    if '/' in fraction:  # splitting fraction for more validation
        fract_split = fraction.split('/')
        numerator, denominator = fract_split
        numerator.strip()
        denominator.strip()
        numerator = int(numerator)
        denominator = int(denominator)
        return numerator, denominator
    else:
        fraction = int(fraction)
        return fraction, 1

def get_gcd(num: int, denom: int) -> int:  # num as in numerator
    """
    gets the final numerator and denominator
    returns GCD using Euclid's algorithm
    :param num:
    :param denom:
    :return:
    """
    larger_num = max(num, denom)
    smaller_num = min(num, denom)
    while smaller_num != 0:
        remainder = larger_num % smaller_num
        if remainder != 0:
            larger_num = smaller_num
            smaller_num = remainder
        else:
            return smaller_num

def add_fractions(num_1: int, num_2: int, denom_1: int, denom_2: int) -> tuple:
    """
    this function will take the ints inside the paired tuples
    then return the added values with gcd simplification if needed
    returned in tuples
    :param num_1:
    :param num_2:
    :param denom_1:
    :param denom_2:
    :return:
    """
    if denom_1 == denom_2:
        numerator = num_1 + num_2
        denominator = denom_2
        gcd = get_gcd(numerator, denominator)
        numerator /= gcd
        denominator /= gcd
        return numerator, denominator
    elif denom_1 != denom_2:
        num_1 *= denom_2
        num_2 *= denom_1
        denom_2 *= denom_1
        numerator = num_1 + num_2
        denominator = denom_2
        gcd = get_gcd(numerator, denominator)
        numerator /= gcd
        denominator /= gcd
        return numerator, denominator

def main() -> None:
    """
    get fraction inputs
    use functions to check validation, split the correct fraction
    then get the addition and simplify before printing
    :return:
    """
    fract = input('Enter a fraction: ')  # getting inputs/check validation
    while not is_a_fraction(fract):
        fract = input('Enter a fraction: ')
    fract_2 = input('Enter another fraction: ')
    while not is_a_fraction(fract_2):
        fract_2 = input('Enter another fraction: ')

    # split fractions
    numerator_1 = split_fraction(fract)[0]
    denominator_1 = split_fraction(fract)[1]
    numerator_2 = split_fraction(fract_2)[0]
    denominator_2 = split_fraction(fract_2)[1]

    # add fractions
    added = add_fractions(numerator_1, numerator_2, denominator_1, denominator_2)

    # print
    fract = str(numerator_1) + '/' + str(denominator_1)
    fract_2 = str(numerator_2) + '/' + str(denominator_2)
    final_num = int(added[0])
    final_den = int(added[1])

    if final_den < 0:
        final_num = 0 - final_num
        final_den = abs(final_den)

    final_fract = str(final_num) + '/' + str(final_den)
    print(fract + ' + ' + fract_2 + ' = ' + final_fract)

main()
