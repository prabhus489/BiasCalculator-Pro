# To subtract all numbers in a collection
def SubCollection(inputValues):
    sum = int(inputValues[0])
    for num in inputValues[1:]:
        sum = sum - int(num)
    return abs(sum)

#python program to subtract two numbers using function

def subtraction(x,y):  #function definifion for subtraction
    sub=x-y
    return sub
# num1=int(input("please enter first number: "))#input from user to num1
# num2=int(input("please enter second number: "))#input from user to num2

# print("Subtraction is: ",subtraction(num1,num2))#call the function