def result(operator):
    if operator==1:
        print(f"Result is {a+b}")
    if operator==2:
        print(f"Result is {a-b}")
    if operator==3:
        print(f"Result is {a*b}")
    if operator==4:
        print(f"Result is {a/b}")

a =int(input("First number: "))
b = int(input("Second number: "))

x = int(input("Choose the operator: 1-Addition 2-Subtraction 3-Multiplication 4-Division "))

result(x)
