def GetPercentFloat(first, second, integer = False):
   percent = first / second * 100
   
   if integer:
       return int(percent)
   return percent

#print(getPercent(3, 9))

GetPercentFloat(3, 9)
#Sample output
#33.33333333333333




