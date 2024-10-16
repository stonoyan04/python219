def sum_of_elements(numbers, exclude_negative=False):
    if exclude_negative:
        return sum(num for num in numbers if num >= 0)
    else:
        return sum(numbers)

numbers_input = input("Enter a list of numbers separated by spaces (e.g., '1 2 3 -4 5 -6'): ")
numbers = list(map(int, numbers_input.split()))

exclude_negatives_input = input("Do you want to exclude negative numbers? (yes or no): ").strip().lower()

if exclude_negatives_input == 'yes':
    result = sum_of_elements(numbers, exclude_negative=True)
else:
    result = sum_of_elements(numbers)

print(f"The sum of the elements is: {result}")