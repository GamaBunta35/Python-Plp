# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1.\n")
        file.write("12345\n")
        file.write("Another line here with some numbers: 987\n")
        print("File 'my_file.txt' created successfully.")
except PermissionError:
    print("Permission denied while creating the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of 'my_file.txt':")
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("\nFile reading process completed.\n")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1.\n")
        file.write("Appending line 2.\n")
        file.write("Appending line 3.\n")
        print("File 'my_file.txt' appended successfully.")
except PermissionError:
    print("Permission denied while appending to the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File appending process completed.")
