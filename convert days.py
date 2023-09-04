# Get the number of days from the user
num_days = int(input("Enter the number of days: "))

# Calculate the number of weeks and remaining days
weeks = num_days // 7
remaining_days = num_days % 7

# Display the result
print(f"{num_days} days is equal to {weeks} weeks and {remaining_days} days.")
