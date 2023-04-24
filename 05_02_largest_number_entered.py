# Largest and smallest number entered

largest = None  
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    num = int(num)  # Convert the input to an integer
    if largest is None or num > largest: # Check the number to see if its the largest so far
        largest = num
    print(num)

print("Maximum:", largest)