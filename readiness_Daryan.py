# Print greeting with name and student ID
print("Hello, I am Daniel Ebrahimi Daryan, and my student ID is R01973327.")

# Define function for mean and maximum
def calculate_mean_and_max(numbers):
    mean = sum(numbers) / len(numbers)
    maximum = max(numbers)
    return mean, maximum

# Call the function and print results
my_list = [10, 20, 30, 40, 50]
mean, max_val = calculate_mean_and_max(my_list)
print(f"Mean: {mean}, Maximum: {max_val}")