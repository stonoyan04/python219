def classify_numbers(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers, odd_numbers


if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")

    number_list = list(map(int, user_input.split()))

    evens, odds = classify_numbers(number_list)

    print("Even numbers:", evens)
    print("Odd numbers:", odds)
