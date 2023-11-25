def remove_chars_in_second_string(first_string, second_string):
    for char in first_string:
        second_string = second_string.replace(char, '')

    return second_string

# Example usage:
first_string = "abc"
second_string = "defabcdef"
result_string = remove_chars_in_second_string(first_string, second_string)

print("Result String:", result_string)
