

#comment out every other tasks if you want to run a specific task that requires user input.


#Task01:Write a Python program that prints "hello world" in a console.
print("Hello World")



#Task02:Write a Python program that prints the summation of 54 and 56. The program must use Python operators and numbers but not use any variables.
print(54+56)



#Task03:Write a Python program that assigns the values "Summer" and 2023 to variables season and year respectively. Then, print the values of both variables in separate lines.
season="Summer"
year=2023
print(season)
print(year)


#Task04:user_name=input("Please enter your name: ")
user_name=input("Please enter your name: ")
print("Your name is",user_name)



#Task05:Write a Python program that reads two integers M and N respectively and finds the value of M^N (or MN) and prints the value exactly as shown in the examples below. Your code should work correctly for any other sample inputs.
M=int(input())
N=int(input())
print(M,"^",N,":",M**N)



#Task06:A sailor has a boat known as Téssares Boat, which has four corners. The boat is capable of carrying goods of any weight as long as there is equal distribution of loads on each corner of the boat - the center area has been occupied by the engine. The sailor needs your help to know the maximum amount of weight he can carry in each shipment. Write a Python program that reads the total weight of the shipment and prints the maximum load (or weight) the boat can take from the given shipment. We can assume that the weight of each good is exactly 1 unit, therefore, the weight of 5 units means there are 5 (loose) items in the shipment.
Total_weight=int(input('Enter total shipment weight: '))
max_weight=Total_weight-(Total_weight%4)
print(max_weight)



#Task07:Write a Python program that reads 3 integers A, B, and C respectively, and then reads a floating point number D. After reading, the program should print the result (as int) using the given formula below.
A=int(input())
B=int(input())
C=int(input())
D=float(input())
result=(A**C)+B*A-(D/3)
print(int(result))



#Task08:Write a python program that takes an integer from the user which represents the number of chocolates that he/she has. He/She decided to distribute the chocolates equally among 3 friends, keeping the remaining chocolates for him/herself. Find out the number of chocolates each friend will receive and the number of chocolates that will be remaining.
number_of_choclates=int(input())
each_frnd_got=number_of_choclates//3
choclates_remained=number_of_choclates%3
print("Each friend will receive",each_frnd_got,"chocolates")
print("The number of remaining chocolates is",choclates_remained)



#Task09:Write a Python program that reads two values M and N from the user respectively and prints the result by joining (concatenating) them in a bottom-up approach as shown in the following example.
M=input()
N=input()
print(N+M)


#Task10:Write a Python program that takes an integer, a float, and another integer number as input from the user and prints the result as shown below. At first, add the first integer number to the float and then concatenate the third input integer number.
number_one=int(input())
number_two=float(input())
added=str(number_one+number_two)
number_three=input()
print("The inputs:",number_one,",",number_two,",",number_three)
print("The result is",added+number_three)



#Task11:Write a Python program that reads an integer and prints "True" if the number is even, otherwise, "False". [Need concept of branching/conditional statements/if-else statements to solve this. These topics may not have been discussed in class yet. Try to solve it if you can.]
number=int(input())
if number%2==0:
  print("True")
else:
  print('False')






