import Add
import Div
import Mult
import Sub

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

choice = input("Add(A), Subtract(S), Multiplication(M)? ")

if choice.lower() == 'a':
    Add.adder(x, y)
elif choice.lower() == 's':
    Sub.subtr(x, y)
elif choice.lower() == 'm':
    Mult.multi(x, y)
elif choice.lower() == 'd':
    Div.divi(x, y)



