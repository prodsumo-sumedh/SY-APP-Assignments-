def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
            
        total_lines = len(lines)
        print(f"Total lines in '{input_filename}': {total_lines}")
        
        first_two_lines = lines[:2]
        
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.writelines(first_two_lines)
            
        print(f"Successfully wrote the first 2 lines to '{output_filename}'.")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

process_file('input.txt', 'output.txt')
