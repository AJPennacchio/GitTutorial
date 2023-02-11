import Add
import Sub

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

choice = input("Add(A), Subtract(S)")

if choice.lower() == 'a':
    Add.adder(x, y)
elif choice.lower() == 's':
    Sub.subtr(x, y)

print("Hello World")