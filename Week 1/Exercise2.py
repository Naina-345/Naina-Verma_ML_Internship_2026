# Assignment 2
# Question 1-Find sum of firdt 10 natural numbers
add=0
for i in range(1,11):
    add=add+i
print(f"the sum of first 10 natural number is {add}")

# Question 2-find factorial of a number
fac=1
n=int(input("enter number whose factorial you want to calculate: "))
for j in range(1,n+1):
    fac=fac*j
print(fac)

# Question 3-print fibonacci series
num=int(input("enter number till which you want to print fibonacci series: "))
a,b=0,1
sum=0
for i in range(num):
    sum=a+b
    print(sum,end=" ")
    a,b=b,sum
print("\n")
    
# Question 4- Find largest among three numbers
num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
num3=int(input("enter number 3: "))
if(num1>num2 and num1>num3):
    print(f"{num1} is largest among the three numbers")
elif(num2>num1 and num2>num3):
    print(f"{num2} is largest")
else:
    print(f"{num3} is largest")
    
#Question 5- Create student result system
# using dictionary to store students details
stu_details={}
stu_details["Name"]=input("enter your name: ")
stu_details["Roll.no"]=int(input("enter your roll num: "))
stu_details["Semester"]=int(input("enter your sem number: "))
print(stu_details)

# using list to input marks
sub=["IDS","DSA","SSPD","WAD"]
marks=[]
for i in range(4):
    mark=int(input("enter marks obtained of {sub[i]}: "))
    marks.append(mark)
d=dict(zip(sub,marks))
print(d)

# to calculate percentage
print(marks)
sum=0
for j in (marks):
    sum=sum+j
print(f"percentage obtained is {(sum/400)*100}")

# to display grade
per=(sum/400)*100
if(per>=90):
    print("Grade A")
elif(per>80):
    print("Grade B")
else:
    print("Grade C")
