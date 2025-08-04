def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        print("Error! Not divisible.")
    return x / y

print("Select operation")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

choice = input("Enter the choice (1/2/3/4):")


a = float(input("Enter the first number:"))

b = float(input("Enter the second number:"))

if choice == '1':
    print(f"The result is {add(a,b)}")
    
elif choice == '2':
    print(f"The result is {subtract(a,b)}")

elif choice == '3':
    print(f"The result is {multiply(a,b)}")

elif choice == '4':
    print(f"The result is {divide(a,b)}")
    
else:
    print("Invalid input.")