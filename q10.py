#input three digit numbers
num = int(input("Enter a three digit number: "))

#extract digits
digit1 = num // 100
digit2 = (num// 10) % 10
digit3 = num % 10

#Reverse number 
reverse = (digit3 * 100) + (digit2 * 10)  + digit1

#Display reuslt
print("Reversed number =", reversed)