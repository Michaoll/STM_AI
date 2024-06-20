def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def remove_unwanted_lines(lines):
    filtered_lines = [line for line in lines if line.strip() not in ("WszedlemDoPetli", "NowyPomiar")]
    return filtered_lines

def write_file(file_name, lines):
    with open(file_name, 'w') as file:
        file.writelines(lines)

# Read the original file
file_name = 'proba_2.txt'
lines = read_file(file_name)

# Remove unwanted lines
filtered_lines = remove_unwanted_lines(lines)

# Write the filtered lines to a new file
new_file_name = 'obrobiony_nowy_test.txt'
write_file(new_file_name, filtered_lines)

print(f"Unwanted lines removed. Processed data saved to {new_file_name}.")
