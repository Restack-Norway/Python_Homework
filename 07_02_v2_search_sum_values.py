# INPUT FILE: Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

# Initialize variables 
count = 0  # store the count of lines with the desired pattern
total = 0  # store the sum of the floating point values

#Run the loop in the positive
for line in fh: #For each line in the file handle
    if line.startswith("X-DSPAM-Confidence:"): # Test the line - does it contain: X-DSPAM-Confidence:
        colon_pos = line.find(':')  # Find the position of the colon
        number_str = line[colon_pos + 1:].strip()  # Extract the floating point value as a string
        number_float = float(number_str)  # Convert the string to a floating point number
        total = total + number_float  # Add the floating point number to the total
        count = count + 1  # Increment the count

#Close the file after the loop
fh.close()

#Output 
average = total / count  # Compute the average of the floating point values
# print ("Count", count)
# print ("Total", total)
print("Average spam confidence:", average)  # Print the result
