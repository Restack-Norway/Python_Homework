#Define the Function to calculate total pay h= hours, r = rate, p = pay test with 45 and 10.50
def computepay(h,r):
    if h > 40: 
        regular_pay = 40 * r
        overtime_pay = (h - 40) * r * 1.5
        p = float (regular_pay + overtime_pay)
    else: 
        p = float (h * r)
    return p

#User input
h = input ("Enter Hours: ")
r = input ("Enter Rate:  ")

#Normalize input 
h = float(h)
r = float(r)
#p = float(p)

#Compute and print Total Pay 
p = computepay(h,r)
print("Pay", p)

