def GetPercentFloat(first, second, integer = False):
   percent = first / second * 100
   
   if integer:
       return int(percent)
   return percent

#print(getPercent(3, 9))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter Second number: "))

GetPercentFloat(num1, num2)
print(GetPercentFloat(num1, num2))
#Sample output
#33.33333333333333




