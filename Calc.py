import Add
import Mult
import Sub

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

choice = input("Add(A), Subtract(S), Multiply(M)")

if choice.lower() == 'a':
    Add.adder(x, y)
elif choice.lower() == 's':
    Sub.subtr(x, y)
elif choice.lower() == 'm':
    Mult.multi(x, y)

print("Hello World")