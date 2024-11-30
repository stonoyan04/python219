def read_file():
    while True:
        try:
            filename = input("Enter the name of the file to open: ")
            if not filename.strip():
                raise ValueError("The filename cannot be empty.")

            with open(filename, 'r') as file:
                content = file.read()
                print("\nFile Contents:")
                print(content)
            return filename, content
        except FileNotFoundError:
            print("File not found. Please try again.")
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid filename.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")


def write_file():
    try:
        new_filename = input("Enter the name of the file to write to: ")
        if not new_filename.strip():
            raise ValueError("The filename cannot be empty.")

        content_to_write = input("Enter the content you want to write to the file: ")
        with open(new_filename, 'w') as file:
            file.write(content_to_write)
        print(f"Successfully wrote to the file: {new_filename}")
    except ValueError as e:
        print(f"Error: {e}. File creation failed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File writing operation is complete.")


def main():
    filename, content = read_file()

    choice = input("Do you want to write to a file? (yes/no): ").strip().lower()
    if choice == 'yes':
        write_to_same_file = input(
            f"Do you want to write to the same file ({filename})? (yes/no): ").strip().lower()
        if write_to_same_file == 'yes':
            try:
                new_content = input("Enter the content you want to add: ")
                with open(filename, 'w') as file:
                    file.write(new_content)
                print(f"Content successfully written to {filename}.")
            except Exception as e:
                print(f"An error occurred while writing to the file: {e}")
            finally:
                print(f"File {filename} has been closed.")
        else:
            write_file()


if __name__ == "__main__":
    main()