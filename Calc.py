

def adder (x, y):
    print( "The sum is", str(x + y) )

def subtr(x, y):
    print("The difference is", str(x - y))

def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))

    choice = input("Add(A), Subtract(S) ")

    if choice.lower() == 'a':
        adder(x, y)
    elif choice.lower() == 's':
        subtr(x, y)

main()
