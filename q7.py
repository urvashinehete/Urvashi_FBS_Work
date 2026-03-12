#Input three degit number
num = int(input("enter a three digit number: "))

#Extract digits
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10

#calculate sum
sum_digits = digit1 + digit2 +digit3

#display result
print("sum of digit=", sum_digits)