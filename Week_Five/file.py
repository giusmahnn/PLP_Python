# File Handling Assignment Script

def write_to_file():
    try:
        # Create and open "my_file.txt" in write mode ('w')
        with open("my_file.pdf", 'w') as file:
            file.write("The act of writing a file with code\n")
            file.write("You're going to see how cool it can be to do that.\n")
            file.write("I am sure you were amazed right.\n")
        print("File created and written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error writing to file: {e}")
    finally:
        print("Exiting write process.")

def read_from_file():
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.pdf", 'r') as file:
            content = file.read()
        print("File content read successfully.")
        print("\n--- File Content ---\n")
        print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error reading the file: {e}")
    finally:
        print("Exiting read process.")

def append_to_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.pdf", 'a') as file:
            file.write("This is the first line writing with python.\n")
            file.write("I felt like adding a second one to it.\n")
            file.write("And then I said why not a third.\n")
        print("File appended successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error appending to file: {e}")
    finally:
        print("Exiting append process.")

# Execute all functions with error handling

if __name__ == "__main__":
    write_to_file()       # Step 1: Create and write to the file
    read_from_file()      # Step 2: Read and display the file content
    append_to_file()      # Step 3: Append to the file
    read_from_file()      # Step 4: Read again to see the updated content
