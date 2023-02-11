def adder(x, y):
    print("The sum is", str(x + y))

def subtr(x, y):
    print("The difference is", str(x - y))

def mult(x, y):
    print("The product is", str(x * y))

def divi(x, y):
    print("The quotient is", str(x / y))

def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))

    choice = input("Add(A), Subtract(S), Multiply(M), Divide(D) ")

    if choice.lower() == 'a':
        adder(x, y)
    elif choice.lower() == 's':
        subtr(x, y)
    elif choice.lower() == 'm':
        mult(x, y)
    elif choice.lower() == 'd':
        divi(x, y)

main()
