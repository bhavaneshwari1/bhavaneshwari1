#Assignment 2
#Calculate Simple interest and compound interest

p = float(input("Enter the principal amount:"))

r = float(input("Enter the annual rate of interst:"))

t = float(input("Enter the tenure in years:"))

si = p*r*t/100

ci = p* (1+r/100)**t - p

print("Simple Interest is:", si)

print("Compound Interest is:", ci)