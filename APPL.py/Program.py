with open("input.txt", "r") as file:
    lines = file.readlines()

# Count lines
line_count = len(lines)
print("Total number of lines:", line_count)

# Extract first two lines
first_two_lines = lines[:2]

# Write first two lines to a new file
with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

print("First two lines written to output.txt")