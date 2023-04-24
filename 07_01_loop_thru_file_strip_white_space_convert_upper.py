# User file input (ask for file)
fname=input("Enter a file:  ")

# Open the file
fh=open(fname)

# Loop through file to strip white space and print the upper case
for line in fh:
    line = line.rstrip() #remove whitepace at end of line
    print(line.upper()) #print upper case contents





