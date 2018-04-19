#!/usr/bin/python3
def get_roman_value(char=''):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    return roman[char]


def roman_to_int(roman_string):
    if roman_string:
        decimal = list(map(get_roman_value, list(roman_string)))
        result = 0
        for i in range(len(decimal) - 1):
            if decimal[i] < decimal[i + 1]:
                result -= decimal[i]
            else:
                result += decimal[i]
        result += decimal[len(decimal) - 1]
        return result
    else:
        return None

