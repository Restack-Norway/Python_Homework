#promt user to enter the score between 0.0 adn 1.0
score = input("Enter Score: ")

#Convert strings to number and error handling
try:
    score = float(score)
except:
    print("enter a number between 0.0 and 1.0")
    quit ()

# Check if the score is within the valid range
if 0.0 <= score <= 1.0:
    if score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    else:
        grade = "F"
    print(grade)
else:
    print("Error: Score is out of range.")