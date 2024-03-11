# Define a function that calculates the average of a list of numbers
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)

# Test the function with a sample list of numbers
sample_numbers = [5, 10, 15, 20, 25]
average = calculate_average(sample_numbers)
print("The average is:", average)
