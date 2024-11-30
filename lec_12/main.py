import random
import time

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@execution_time_decorator
def create_file(filename):
    with open(filename, 'w') as file:
        for _ in range(100):
            numbers = [str(random.randint(1, 100)) for _ in range(20)]
            file.write(" ".join(numbers) + "\n")

@execution_time_decorator
def filter_and_write_back(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    filtered_lines = []
    for line in lines:
        numbers = list(map(int, line.split()))
        filtered_numbers = list(filter(lambda x: x > 40, numbers))
        filtered_lines.append(" ".join(map(str, filtered_numbers)))

    with open(filename, 'w') as file:
        for line in filtered_lines:
            file.write(line + "\n")

@execution_time_decorator
def read_file_as_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

if __name__ == "__main__":
    filename = "random_numbers.txt"

    create_file(filename)
    filter_and_write_back(filename)

    print("\nReading the file as a generator:")
    generator = read_file_as_generator(filename)
    for i, line in enumerate(generator):
        print(f"Line {i + 1}: {line}")
        if i >= 4:
            break