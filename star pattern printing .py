# Function to print the pattern
def print_star_pattern(rows, columns):
    for i in range(rows):
        for j in range(columns):
            print("*", end=" ")
        print()

# Set the number of rows and columns
rows = 5
columns = 5

# Call the function to print the pattern
print_star_pattern(rows, columns)
