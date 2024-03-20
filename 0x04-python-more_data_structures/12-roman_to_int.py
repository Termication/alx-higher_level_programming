#!/usr/bin/python3
def to_subtract(numbers_list):
    to_subtract_value = 0
    max_number = max(numbers_list)

    for number in numbers_list:
        if max_number > number:
            to_subtract_value += number

    return (max_number - to_subtract_value)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    roman_numerals_keys = list(roman_numerals.keys())

    total = 0
    last_roman_value = 0
    numbers_list = [0]

    for char in roman_string:
        for roman_numeral in roman_numerals_keys:
            if roman_numeral == char:
                if roman_numerals.get(char) <= last_roman_value:
                    total += to_subtract(numbers_list)
                    numbers_list = [roman_numerals.get(char)]
                else:
                    numbers_list.append(roman_numerals.get(char))

                last_roman_value = roman_numerals.get(char)

    total += to_subtract(numbers_list)

    return (total)
