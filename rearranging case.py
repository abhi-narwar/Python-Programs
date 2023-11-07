input_str = "aBcDeFgHiGk"

lower = ''
upper = ''

for char in input_str:
    if char.islower():
        lower += char
    else:
        upper += char
    
result_str = lower + upper
print(result_str)

