# Initialize largest and smallest to None
largest = None
smallest = None

# Loop infinitely until the user enters "done"
while True:
    # Ask the user to enter a number
    num = input("Enter a number: ")
    
    # Check if the user entered "done", and exit the loop if so
    if num == "done":
        break
    
    # Convert the user's input to an integer (if possible)
    try:
        num = int(num)
    except:
        # If the user's input cannot be converted to an integer, ignore it and continue the loop
        print("Invalid input")
        continue
    
    # If largest is None (i.e. it has not been set yet), set it to the user's input
    if largest is None:
        largest = num
    # Otherwise, check if the user's input is greater than the current largest, and update largest if so
    elif num > largest:
        largest = num
        
    # If smallest is None (i.e. it has not been set yet), set it to the user's input
    if smallest is None:
        smallest = num
    # Otherwise, check if the user's input is less than the current smallest, and update smallest if so
    elif num < smallest:
        smallest = num

# Print the largest and smallest values
print("Maximum", largest)
print("Minimum", smallest)
