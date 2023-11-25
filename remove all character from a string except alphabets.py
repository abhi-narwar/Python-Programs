str='abdc123 abhi'
filtered_str=''.join(char, for char in str if char.isalpha() or char.isspace())
print(filtered_str)
