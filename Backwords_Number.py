number = int(input("Enter a number"))
backwords_number = 0

while number != 0:
    number_digit = number % 10
    backwords_number = backwords_number * 10 + number_digit
    number = number//10

print("Your reversed number is", backwords_number)
