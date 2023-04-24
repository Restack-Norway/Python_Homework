fname = input("Enter file name: ") # Read the file
fh = open(fname) #open the file
lst = list() #Create an empty list

for line in fh: #Go thru the list
    words = line.split() #Split the line into a list of words
    for word in words:   #Check each word in the line and append it to the list if it's not already there.
        if word in lst:  #check to see if the word is already in the list.
            continue     #Continue back to the toop
        lst.append(word) #If not, then add it. 

# Sort the list of unique words in alphabetical order
lst.sort()

# Print the sorted list of unique words
print(lst)
