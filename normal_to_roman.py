def normal_to_roman(n):
    if not isinstance(n, int) or n <= 0 or n >= 4000:
        return "Invalid number, insert a number betwen 1 to 3999"
    
    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    
    roman_numeral = ""
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while n >= value:
            roman_numeral = numeral
            n -= value
    return roman_numeral 