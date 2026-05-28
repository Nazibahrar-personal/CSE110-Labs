#comment out every other tasks if you want to run a specific task that requires user input.


#Task01:Write the Python code of a program that reads two numbers from the user, and prints their sum, product, and difference.
Number1=int(input('Enter number one:'))
Number2=int(input('Enter number two:'))
print('Sum:',Number1+Number2)
print('Product:',Number1*Number2)
print('Difference:',Number1-Number2)



#Task02:Write the Python code of a program that reads the radius of a circle and prints its circumference and area.
from ast import For, If
import math
radius=int(input("enter the value of radius: "))
area=math.pi*radius**2
circumference=2*math.pi*radius
print("Area of the circle is:",area)
print("Circumference of the circle is:",circumference)



#Task03:Write the Python code of a program that reads two numbers from the user. The program should then print "First is greater" if the first number is greater, "Second is greater" if the second number is greater, and "The numbers are equal" otherwise.
number1=int(input("enter the first number: "))
number2=int(input("enter the second number: "))
if number1>number2:
    print("First is greater")
elif number2>number1:
    print("Second is greater")
else:
    print("The numbers are equal")
    
    
    
#Task04:Write the Python code of a program that reads two numbers, subtracts the smaller number from the larger one, and prints the result.
number1=int(input("enter the first number: "))
number2=int(input("enter the second number: "))
if number1>number2:
    print(number1-number2)
elif number2>number1:
    print(number2-number1)
else:
    print(0)



#Task05:Write the Python code of a program that reads a number, and prints "The number is even" or "The number is odd", depending on whether the number is even or odd.
number=int(input("enter a number: "))
if number%2==0:
    print("The number is even")
else:
    print("The number is odd")



#Task06:Write the Python code of a program that reads an integer as input from the user, and prints the integer if it is a multiple of 2 OR 5 and prints "Not a multiple of 2 OR 5" otherwise.
number=int(input("enter a number: "))
if number%2==0 or number%5==0:
    print(number)
else:
    print("Not a multiple of 2 OR 5")
    
    
    
#Task07:Write the Python code of a program that reads an integer, and prints the integer it is a multiple of either 2 or 5 but not both. If the number is a multiple of 2 and 5 both, then print "Multiple of 2 and 5 both". For all other numbers, the program prints "Not a multiple we want".
number=int(input("enter a number: "))
if number%2==0 and number%5==0:
    print("Multiple of 2 and 5 both")
elif (number%2==0 and number%5!=0) or (number%2!=0 and number%5==0):
    print(number)
else:
    print("Not a multiple we want")



#Task08:Write the Python code of a program that reads an integer, and prints the integer if it is a multiple of 2 AND 5 and prints "Not multiple of 2 and 5 both" otherwise.
number=int(input("enter the number : "))
if number%2==0 and number%5==0:
    print(number)
else:
    print("Not multiple of 2 and 5 both")



#Task09:Write the Python code of a program that finds the number of hours, minutes, and seconds in a given number of seconds. The number of seconds is taken as input from the user. 
total_seconds=int(input("enter the number of seconds: "))
hours=total_seconds//3600
minutes=(total_seconds%3600)//60
seconds=(total_seconds%3600)%60
print("Hours:",hours)
print("Minutes:",minutes)
print("Seconds:",seconds)



#Task10:Write a Python program to compute and display a person’s weekly salary as determined by the following conditions:
#If the hours worked is less than or equal to 40, then the person receives Tk 200 per hour.
#If the hours worked is greater than 40, then the person receives Tk 8000 plus Tk 300 for each hour worked over 40 hours.
#The program should request the hours worked as an input from the user and display the salary as output. You need to make sure that user input is valid. For example, a person cannot work for -5 hours or more than 168 hours in a week. So, the valid hours range is 0 to 168. For invalid hours, print outputs as given in the samples below.
hours_worked=int(input('enter the hours of work: '))
if hours_worked<0:
    print("Hour cannot be negative")
elif hours_worked>168:
    print("Impossible to work more than 168 hours weekly")

elif 0<=hours_worked<=40:
    salary=hours_worked*200
else:
    salary=8000+(300*hours_worked-40)
print(salary)



#Task11:Suppose the following expressions are used to calculate the values of L for different values of S:

# L = 3000-125S^2 if S < 100
# L = 12000/(4+S^2)/14900 if S>=100


# Write the Python code of a program that reads a value of S and then calculates the value of L.


S = int(input("Enter the value of S: "))
if S < 100:
    L = 3000 - 125 * S**2
else:
    L = 12000 / (4 + S**2) / 14900
print("The value of L is:", L)



#Task12:Write a Python program that takes an hour from the user as input and tells it is time for which meal.
#• The user will input the number in a 24-hour format. So, 14 means 2 pm, 3 means 3 am, 18 means 6 pm, etc.
#• Valid inputs are 0 to 23. Inputs less than 0 or more than 23 are invalid in 24-hour clock.
#• Assume, input will be whole numbers. For example, 3.5 will NOT be given as input.
# Input range: Message to be printed
# 4 to 6: Breakfast
# 12 to 13: Lunch
# 16 to 17: Snacks
# 19 to 20: Dinner
# For all other valid inputs, say "Patience is a virtue"
# For all other invalid inputs, say "Wrong time"




hour = int(input("Enter the hour (0-23): "))

if 0<=hour<=23:
    if 4<=hour<=6:
        print("Breakfast")
    elif 12<=hour<=13:
        print("Lunch")
    elif 16<=hour<=17:
        print("Snacks")
    elif 19<=hour<=20:
        print("Dinner")
    else:
        print("Patience is a virtue")
else:
    print("Wrong time")
    


#Task13:Write the Python code of a program that reads a student’s mark for a single subject, and prints out the corresponding grade for that mark. The mark ranges and corresponding grades are shown in the table below. You need to make sure that the mark is valid. For example, a student cannot receive -5 or 110 marks. So, the valid marks range from 0 to 100.

# 90 or above :A
# 80-89 :B
# 70-79 :C
# 60-69 :D
# 50-59 :E
# Below 50 :F


mark = int(input("Enter the student's mark (0-100): "))
if 0 <= mark <= 100:
    if mark >= 90:
        print("Grade: A")
    elif mark >= 80:
        print("Grade: B")
    elif mark >= 70:
        print("Grade: C")
    elif mark >= 60:
        print("Grade: D")
    elif mark >= 50:
        print("Grade: E")
    else:
        print("Grade: F")
else:
    print("Invalid mark. Please enter a mark between 0 and 100.")



#Task14:Suppose, your friend is building an automated car called “Besla”. He needs to fix the programming of the car so that it runs at a proper speed. Now, write a python program that takes 2 inputs (distance in meters and time in seconds). The program should then print the velocity in kilometers per hour of that car. Also, it should print whether the car is working properly based on the following chart.

# Less than 60 km/h:Too slow. Needs more changes.
# Between 60 km/h to 90 km/h:Velocity is okay. The car is ready!
# Greater than 90 km/h:Too fast. Only a few changes should suffice.

distance = int(input("Enter the distance in meters: "))
time = int(input("Enter the time in seconds: "))

velocity = (distance / time) * 3.6 

print(f"The velocity of the car is {velocity:.2f} km/h.")

if velocity < 60:
    print("Too slow. Needs more changes.")
elif 60 <= velocity <= 90:
    print("Velocity is okay. The car is ready!")
else:
    print("Too fast. Only a few changes should suffice.")
    
    

#Task15:Write a python program that takes the CGPA and no of credits completed by a student and prints whether the student is eligible for a waiver and of what percentage.
# To be eligible for a waiver, a student must have completed at least 30 credits and earned a CGPA greater or equal to 3.8. If not, please print "The student is not eligible for a waiver".

# 3.80 - 3.89:25 percent
# 3.90 - 3.94:50 percent
# 3.95 - 3.99:75 percent
# 4.00       :100 percent


cgpa = float(input("Enter the CGPA: "))
credits = int(input("Enter the number of credits completed: "))

if credits >= 30 and cgpa >= 3.8:
    if 3.80 <= cgpa <= 3.89:
        print("The student is eligible for a waiver of 25 percent.")
    elif 3.90 <= cgpa <= 3.94:
        print("The student is eligible for a waiver of 50 percent.")
    elif 3.95 <= cgpa <= 3.99:
        print("The student is eligible for a waiver of 75 percent.")
    elif cgpa == 4.00:
        print("The student is eligible for a waiver of 100 percent.")
else:
    print("The student is not eligible for a waiver.")
    



#Ungraded tasks

#Task20:Write the Python code of a program that reads an integer, and prints the integer if it is a multiple of NEITHER 2 NOR 5.
# For example, 1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39 …
number=int(input("enter a number: "))
if number%2!=0 and number%5!=0:
    print(number)
else:
    print("No")



#Task21:Write the Python code of a program that reads an integer, and prints the integer if it is NOT a multiple of 2 OR NOT a multiple of 5.
# For example, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22\
number=int(input("enter a number: "))
if number%2!=0 or number%5!=0:
    print(number)
else:
    print("No")



#Task22:Fiona has recently started acrylic painting and she is planning to order a few canvases and paints from an online stationery shop. The price of each 10 x 10 sized canvas is 120 tk and the price of each 25 ml paint tube is 75 tk. Depending on the total amount ordered from the shop, she will get some discounts. The table below shows the discount she will get on her total amount.
# 0 – 299:No Discount
# 300 - 499:10
# 500 - 749:20
# 750 - 999:50
# >= 1000  :150
# Write a python program and take two inputs from the user. The first input will be the number of canvases and the second input will be the number of paint tubes ordered. Based on the price of each item, calculate the total amount that Fiona needs to pay including the discount
num_canvases=int(input("Enter the number of canvases: "))
num_paint_tubes=int(input("Enter the number of paint tubes: "))

total_amount = (num_canvases * 120) + (num_paint_tubes * 75)

if total_amount >= 1000:
    discount = 150
elif total_amount >= 750:
    discount = 50
elif total_amount >= 500:
    discount = 20
elif total_amount >= 300:
    discount = 10
else:
    discount = 0

final_amount = total_amount - discount

print(f"The total amount is {total_amount} tk.")
print(f"The discount is {discount} tk.")
print(f"The final amount is {final_amount} tk.")



#You are designing a robot that can calculate the temperature and guess the season. Write a Python program that takes a number as input, representing the temperature in degrees Fahrenheit, and converts it into degrees Celsius, and then prints the season based on the following table:
# Less than 20 degrees:Winter
# Between 20 degrees and 25 degrees (inclusive):Autumn
# Greater than 25 degrees and less than 30 degrees:Spring
# Greater than or equal to 30 degrees:Summer

#Use the following formula to convert the temperature:(degrees Celsius) = ((degrees Fahrenheit) - 32) * 0.56

temperature_f = float(input("Enter the temperature in degrees Fahrenheit: "))
temperature_c = (temperature_f - 32) * 0.56

if temperature_c < 20:
    season = "Winter"
elif 20 <= temperature_c <= 25:
    season = "Autumn"
elif 25 < temperature_c < 30:
    season = "Spring"
else:
    season = "Summer"

print(f"The temperature in degrees Celsius is {temperature_c:.2f}.")
print(f"The season is {season}.")
