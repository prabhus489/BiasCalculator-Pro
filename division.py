# To divide all numbers in a collection
def DivideCollection(inputValues):  
    sum = int(inputValues[0])
    for num in inputValues[1:]:
        dividend = int(num)
        if dividend > 0:
            sum = sum / dividend
    return int(sum)

def divNum(a,b):#function definision
  return a/b
# For testing
# num1=int(input("Please input the number for num1: "));
# #Ask and reading the input from user for num1
# num2=int(input("Please input the number for num2: "));
# #Ask and reading the input from user for num2
# print("Division of given numbers is:",divNum(num1,num2))
# #call the function