def count_characters(input_string):
    vowels = consonants = digits = white_space = 0

    for char in input_string:
        if char.lower() in 'aeiou':
            vowels += 1
        elif char.isalpha():
            consonants += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            white_space += 1

    return vowels, consonants, digits, white_space


my_string = "Hello 123, World!"
vowels, consonants, digits, white_space = count_characters(my_string)

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("White spaces:", white_space)
