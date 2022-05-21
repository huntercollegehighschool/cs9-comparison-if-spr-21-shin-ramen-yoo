'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''

number1 = int(input("Enter a number: "))
first = number1

number2 = int(input("Enter another number: "))
middle = number2

number3 = int(input("Enter another number: "))
last = number3

if first < middle and first < last:
  print("The smallest number is", first)
elif middle < first and middle < last:
  print("The smallest number is", middle)
elif last < first and last < middle:
  print("The smallest number is", last)
