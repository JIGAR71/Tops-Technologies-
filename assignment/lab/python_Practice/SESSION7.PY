



#SESSION 7 — Conditional Statements Topics: if, elif, else Nested conditions Demo: If revenue &gt; target ? print “Achieved”

"""
Conditional statement kya hota hai?

Condition ke base par decision lena

Real life:

Agar marks ≥ 35 → Pass

Agar balance < 0 → Warning

Agar sales > target → Achieved

Python me ye kaam if–else karta hai
"""

#BASIC if STATEMENT


sales = 5000               
if sales>4000:
    print("Targate Achiv")

"""
if → condition check

sales > 40000 → True / False

True hua → print chalega

False hua → kuch nahi hoga
"""

#if – else STATEMENT

sales= 200
if sales > 250:
    print("Yes")
else:
    print("No") 


#if – elif – else (Multiple conditions)

mark = 75
if mark >= 90:
    print("Grad A")
elif mark >= 85:
    print("Grad B")
elif mark >= 75:
    print("Grad C")
else:
    print("Fail")

#REAL DATA ANALYTICS DEMO

sales = 1200
target = 1201

if sales < target:
    print("Target Achiv")
else:
    print("Not Achiv ")

"""
COMPARISON OPERATORS (Very Important)
Operator       Meaning
>	        Greater than
<	        Less than
>=	        Greater or equal
<=	        Less or equal
==	        Equal
!=	        Not equal
"""

#LOGICAL OPERATORS
age = 25

if age >=18 and age <=60:
    print("Eligible")


#PRACTICE

age = 27
if age > 18:
    print("Eligible")
else:
    print("Not Eligible" )

# EX
sales = 45000
target = 50000

if sales > target:
    print("Achieved")
else:
    print("Not Achieved")



#NESTED if
"""
if ke andar ek aur if

Jab decision 2 ya zyada level ka ho, tab nested if use hota hai.

Real-life example:

Pehle check → user logged in?

Phir check → user admin hai ya nahi?
"""

#BASIC NESTED IF EXAMPLE

age = 78
if age >=18:
    if age<=60:
        print("Eligable")
    else:
        print("Age above limit")
else:
    print("Underage")

#REAL DATA ANALYTICS EXAMPLE

revenue = 120000
target = 100000
bonus_limit = 150000
print("Total Revenue",revenue)
print("TOtal Traget:",target)
print("Bounus Limit:",bonus_limit)

if revenue>target:
    print("Traget Achiv")
    if revenue >bonus_limit:
        print("bonus Eligable")
    else:
        print("No Bonus")
else:
    print("Traget Not Achiv")


#NESTED IF vs elif

#mark = int(input("Enter The Mark:"))
if mark>=95:
    print("Grad A")
elif mark>=75:
    print("Grad B")
else:
    print("Faild")


#PRACTICE

balance = 5000
withdraw = 3000
Low_amount = 1000

if balance >=withdraw:
    print("Withdrawal allowed")
    if balance - withdraw< Low_amount:
        print("Low Balance Warning")
else:
    print("Insufficient Balance")

# (mene yaha if balance >withdraw "="  lganana bhul gaya )


#LOGICAL OPERATORS
"""
Logical operators multiple conditions ko combine karne ke kaam aate hain.
Python me 3 logical operators hote hain:
1️⃣ and
2️⃣ or
3️⃣ not
"""

#1 and

#age = int(input("Enter The Age:"))
if age>= 18 and age<= 60:
    print("Eligable")
else:
    print("Not Eligable")

# 2 or
"""
role = str(input("Enter The Id:"))
if role == "admin" or role != "manger":
    print("Access he Laptop")
else:
    print("Access denied")
"""
# 3 not

is_active = False

if not is_active:
    print("User is inactive")

#REAL DATA ANALYTICS EXAMPLE

sales = 55000
target = 50000
region = "North"

if sales > target and region == "North":
    print("Bouns Eligable:")
else:
    print("Not Eligable")


#COMBINE and + or
"""
age= int(input("Enter The Age::"))
employe_id = True

if (age >= 18 and age <= 60) and employe_id:
    print("Eligabel")
else:
    print("Not Eligable")
"""
#PRACTICE
"""
username = input("Enter The Usename:")
password = int(input("Enter The Password:"))

if username == "admin" and password == 1234:
    print("Login Successful")
else:
    print("Login Failed")
"""

#PRACTICE

age = int(input("Enter age: "))
citizen = input("Are you Indian (yes/no): ")

if age >= 18 and citizen == "yes":
    print("Eligible to Vote")
else:
    print("Not Eligible")


# END
age = int(input("Enter The Age"))





































