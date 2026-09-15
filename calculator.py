###เครื่องคิดเลขคณิตศาสตร์###

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#-------Main function to run the calculator-------#
print ("Simple calculator by Chaiwat :")
num1 = float(input("กรอกตัวเลขที่ 1 ที่นี่: "))
num2 = float(input("กรอกตัวเลขที่ 2 ที่นี่: "))

print("-"*25)
print("Addition (+):", add(num1, num2))