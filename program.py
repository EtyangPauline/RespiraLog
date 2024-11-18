def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as input_file:
            content = input_file.read()  # Read content from the file
            modified_content = content.upper()  # Modify content (e.g., convert to uppercase)

        # Write the modified content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        print(f"File successfully written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    
    except IOError:
        print(f"Error: There was an issue reading or writing the file.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask user for filenames
input_filename = input("Program file: ")
output_filename = input("program.env: ")

read_and_write_file(input_filename, output_filename)
