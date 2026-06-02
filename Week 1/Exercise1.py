# ML Internship assignment 1
# Question 1 - Find area of rectangle
len=int(input("enter length of rectangle: "))
bre=int(input("enter breath of rectangle: "))
print(f"Area of rectangle is {len} x {bre} = {len*bre} \n")

# Question 2- Find simple interest (S.I. = PTR/100)
P=int(input("enter principle(in dollar): "))
T=int(input("enter time(in years): "))
R=int(input("enter rate: "))
print(f" The simple interest(PTR/100) is : {(P*T*R)/100}\n")

# Question 3- Convert temperture from celsius to fahrenheit
# formula to convert from degree celsius to fahrenheit is F=9*C/5+32
temp=int(input("enter temp which you want to convert from celsius to fahrenheit: "))
print(f"{temp}C= {((9*temp)/5)+32}F \n")

# Question 4- Calculate average of three numbers
num1,num2,num3=2,6,8
print(f"average of three numbers is {num1+num2+num3/3}\n")

# Question 5-Find square and cube of a number
num=int(input("enter number"))
print(f" The square of {num} is {num}x{num} = {num*num} \n The cube of {num}  is {num}x{num}x{num} = {num*num*num} \n")

# Question 6- Swap numberes without third variable
val1,val2=4,8
print(f"values before swapping are {val1}, {val2}")
val1,val2=val2,val1
print(f"values after swapping are {val1}, {val2} \n")

# question 7 Create a Student Report Program that take student details using input(), Store marks in variables, /
# Calculate total and percentage , Use comments, Use proper indentation
Name=input("Enter your Name:")
Roll_no=int(input("enter your roll number: "))
Branch=input("rnter your branch: ")
sem=int(input("enter your semester number: "))
# using dictionary to store marks
Marks={"Maths":98,"DSA":91,"Physics":96,"SSPD":99}
# total of marks obtained is
sum=0
for i in Marks.values():
    sum=sum+i
print(f"total marks obtainrd are {sum}")
# percentage is sum/total x 100
print(f"percentage of marks is {(sum/400)*100}")
