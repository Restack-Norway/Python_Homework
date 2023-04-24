def count_lines(fh):
    count = 0
    for line in fh:
        if line.startswith("X-DSPAM-Confidence:"):
            count = count + 1
    return count

def sum_values(fh):
    total = 0
    fh.seek(0)  # Reset the file pointer to the beginning of the file
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        colon_pos = line.find(':')
        number_str = line[colon_pos + 1:].strip()
        number_float = float(number_str)
        total = total + number_float
    return total

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = count_lines(fh)  # Call the count_lines function
total = sum_values(fh)  # Call the sum_values function

fh.close()  # Close the file

average = total / count  # Compute the average of the floating point values
print("Average spam confidence:", average)  # Print the result
