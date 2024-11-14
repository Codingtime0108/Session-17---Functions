num1 = int(input("Enter any number:"))
num2 = int(input("Enter another number:"))
print ("a. Add")
print ("b. Subtract")
print ("c. Multiply")
print ("d. Divide")
choose = input("Please select ur operation:")

def add(num1,num2):
    addition = num1 + num2
    print(addition)

def sub(num1,num2):
    subtract = num1 - num2
    print(subtract)

def times(num1,num2):
    times = num1 * num2
    print(times)

def div(num1,num2):
    division = num1/num2
    print(division)
    
if choose == "a":
    add(num1,num2)
elif choose == "b":
    sub(num1,num2)
elif choose == "c":
    times(num1,num2)
elif choose == "d":
    div(num1,num2)
