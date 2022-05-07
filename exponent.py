# Python Program to find Power of a Number

number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))

power = 1
i = 1

while(i <= exponent):
    power = power * number
    i = i + 1
    
print("The Result of {0} Power {1} = {2}".format(number, exponent, power))