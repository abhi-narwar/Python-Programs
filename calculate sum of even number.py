# Function to calculate the sum of even numbers
def sum_of_even_numbers(n):
    sum = 0
    for i in range(2, n + 1, 2):
        sum += i
    return sum

# Get user input for the upper limit
try:
    upper_limit = int(input("Enter a positive integer: "))
    
    if upper_limit <= 0:
        print("Please enter a positive integer.")
    else:
        result = sum_of_even_numbers(upper_limit)
        print(f"The sum of even numbers from 1 to {upper_limit} is: {result}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
