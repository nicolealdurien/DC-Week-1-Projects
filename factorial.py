#Assignment 1 - Factorial
def factorial():
    number = int(input("Enter a number: "))
    factorial = 1
    if number < 0:
        print("Factorials cannot be performed on negative numbers.")
    else:
        for i in range(1, number + 1):
            factorial *= i
    print(factorial)
factorial()

