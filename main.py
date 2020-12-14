#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator")
total_bill = input("What was the total bill?\n")
tip_percentage = input("What percentage tip would you like to give?\n")
no_of_people = input("Enter the number of people?\n")
#Calculate the amount included with tip
bill_with_tip = float(total_bill) + (float(total_bill)*int(tip_percentage)) / 100
#Devide the amount with no of people
divided_tip = bill_with_tip / int(no_of_people)
#Round the amount into two decimals
rounded_tip = round(divided_tip, 2)
#Print the amount
print(f"Each person should pay ${rounded_tip}")
