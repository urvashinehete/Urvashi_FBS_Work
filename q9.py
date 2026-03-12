#Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number"))

print("Before swapping:")
print("a =", a)
print("b =", b)

#swapping
a, b = b,a

print("After swapping:")
print("a =", a)
print("b =", b)