def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

#Example
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers) #this will return 0
print(f"The average is: {average}")

my_numbers = [10, 20, 30, 40, 50, 'a']
average = calculate_average(my_numbers) #this will throw an error
print(f"The average is: {average}")