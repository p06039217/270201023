# Write a Python program that asks the user for an integer and prints the sum of the last two digits of the number. Note: If it is a single-digit number, assume it has 0 at the beginning, e.g. 07 for 7.

number = int(input("enter a integer: "))

first_digit = number%10
second_digit = (number % 100)//10

sum = first_digit + second_digit

print(sum)


