"""
#REAL DATA ANALYTICS EXAMPLE

#Product	Price	   Discount
#"Samsung"	"25000"	   "10"
#"Iphone"	"80000"    "5"

Product= "Samsung"
Price = 25000
Discount = 10

Price = int(Price)
Discount = int (Discount)

Discount_amount = (Price*Discount)/100
final_amount = Price-Discount_amount
print("Product Name:", Product)
print("Product Price:", Price)
print("Product Total Discount:", Discount)
print("Discount Amount:", Discount_amount)
print("Final Amount:",final_amount)

"""


"""
#Convert "1200" to int and calculate 18% GST.

price= 1200
price= int(price)
gst= (price*18)/100
finla_amount = price-gst
print("GST Amonut:",gst)
print("Final Amount:",finla_amount)



x= 25.5
x= float(x)
print(x*2)

x= 25.5
y= 2
z= x*y
print(z)


x="4500.75"
x= float(x)
x_value = (x*10)/100
final_value=x-x_value
print("Final Value:",final_value)


product = "Laptop"
price = "60000.50"
discount = "12"

price = float (price)
discount= int (discount)

discount_price = (price*discount)/100
final_price= price-discount_price
print("Discount Price:",discount_price)
print("Final Discount price:" , final_price)




#Tumhe Python me ye karna hai:price ko float me convert karna gst ko int me convert karna
#GST amount calculate karna:
#gst_amount = price * gst / 100
#Final price (price + gst_amount) print karna
#Output exactly is format me print karna:

item= "Smartwatch"
price = 7999.99
gst = 18

price = float(price)
gst = int(gst)

gst_discount= (price*gst)/100
final_amount= price+gst_discount
print("GST Discount:",gst_discount)
print("Final Amount:", final_amount)



#String Indexing
#Har string ke characters ka index number hota hai. Index 0 se start hota hai.

Name="Jigar"
print(Name[0])
print(Name[1])

#String Slicing
print(Name[0:3])
print(Name[1:3])
print(Name[2:3])
print(Name[0:5])
print(Name[:])

#Negative Indexing
print(Name[-3])
print(Name[-5])


#Important String Methods

# agr kisi bhi word ko small letar se learg letar me karna ho to
#upper() – Capital letters

Name= "jigar"
print(Name.upper())


# lower() ke liye

Name="JIGAR"
print(Name.lower())


# strip() – Extra spaces hataana

product= "   Jigar  Panchal"
print(product.strip())

#replace() – Text replace karna

Name= "Jigar-Panchal"
Cilen_Name = Name.replace("Jigar","Kigar")
print(Cilen_Name)
# Jigar ki jagha yaha hamne Kigar kar diya replace me

# EX1 replace()

Car ="Jeep-AA"
Change_Car= Car.replace("AA","AC")
print(Change_Car)

# EX 2 replace()

bname= "TOOPS-TECH"
change_bname = bname.replace("TOOPS","TOPS")
print(change_bname)



# split() – String ko list me todna

data = "apple,kiwi,banana"
friuts = data.split("1,2,3")
print(friuts)


#String Formatting

#f-string — 
name = "jiagr"
Age = '21'
print(f"my name is {name} and age is {Age}")


name = "Jigar"
city = "Ahemdabad"
order = '15'
print(f"Custuber {name} form {city} placed {order} order")


# EX - REAL DATA ANALYTICS EXAMPLE

product = "Laptop"
price = 50000
discount = 10

product_discount=(price*discount)/100
final_price = price-product_discount
print(f"Product Discount:{product_discount}")
print(f"Final Amount:{final_price}")





#SESSION 5 — LISTS & TUPLES

#ist = ek variable ke andar multiple values store karna

sales=[1200,1000,2300,4322,2478]
print(sales[1])

#LIST INDEXING
print(sales[0:3])

#LIST ko UPDATE
sales[2]=2500
print(sales)

#IMPORTANT LIST FUNCTIONS

#append() — end me value add karna
sales=[1200,1000,2340,4325,2480]
sales.append(1000)
print(sales)


#extend() — multiple values add karna
sales.extend([5555,4444,3333])
print(sales)

#pop() — value remove karna
saless=[1200,1000,2340,4325,2480]
saless.pop(0)
print(saless)

#LOOP ke saath LIST

MondayToSatrday_sales=[1222,2200,5120,2390,3210,6599]
Sunday_sales=8732
for i in MondayToSatrday_sales:
    Sunday_sales=Sunday_sales+i
print(f"Total sales:{Sunday_sales}")    

#EX- 
customers = ["Amit", "Ravi", "Neha"]
customers.append("Gita")
customers.pop(1)
print(customers)


#enumerate() — KYA HAI? KYU USE HOTA HAI

customers = ["Amit", "Ravi", "Neha"]
for index, c in enumerate(customers, start=1):
    print(f"{index} Name:{c}")


#EX-
products = ["Mobile", "Laptop", "Tablet"]
for index, p in enumerate(products, start=1):
    print(index,p)


#WHILE LOOP
    #Jab tak condition TRUE hai, tab tak loop chalta rahega.
i = 1
while i<= 5:
    i =i+1
    print(i)
    

#WHILE LOOP WITH LIST

products = ["Mobile", "Laptop", "Tablet"]
i = 0
while i <len(products):
    print(products[i])
    i = i+1

#REAL DATA ANALYTICS EXAMPLE

sales= [12,3,5,8,2]
i= 0
total = 10

while i < len (sales):
    total=total+sales[i]
    i=i+1
print("Total sales:",total)
   
    
#BREAK (Loop todna)

i = 1
while i <=5:
    if i == 3:
        break
    print(i)
    i =i+1


#CONTINUE (Skip current loop)

i = 0
while i < 5:
    i = i+1
    if i == 3:
        continue
    print(i)
        
i = 0
while i < 5:
    i = i+1
    if i == 3:
        continue
    print(i)
    
#PRACTICE
numbers = [10, 20, 30, 40]
i = 0
total= 0

while i <len(numbers):
    total=total+numbers[i]
    i=i+1
print(total)




#extend() —
    #Ek list ke andar doosri list ke saare elements add kar deta hai
day1 = [1200,3400]
day2 = [1500,2300]
day1.extend(day2)
print(day1)

#EX-
ids_jan = [101, 102]
ids_feb = [103, 104, 105]

ids_jan.extend(ids_feb)
print(ids_jan)




a = [10, 20]
b = [30, 40]
a.append(b)
print(a)

nums = [5, 10, 15, 20, 25]
nums.pop(2)
print(nums)


cities = ["Delhi", "Mumbai", "Pune"]
for index , c in enumerate(cities, start=1):
    print(index,c)



prices = [100, 200, 300]
i =0
total=0
while i <len(prices):
    total=total+prices[i]
    i=i+1
print(total)


months = ("Jan", "Feb", "Mar")
months = months+("Apr",)
print(months)


#tuple

distance=int(input("Enter disatance:"))
             
if distance <=5:
    print("Fare:$2")

elif distance <=10:
    print("Fare:$20")

elif distance <=15:
    print("Fare:$20")

else:
    print("Fare:$ kangal ho jayega")


phone=int(input("select any one phone \n 1-Nokiy A7000 \n 2-moto G35 5G \n 3-OnePlus Nord CE4 Lite 5G \n 4-Poco X7 \n 5-i phone 16 pro \n :"))

if phone <= 1:
    print("Nokiy A7000 price: 1200rs")

elif phone <=2:
    print("moto G35 5G price: 12000rs")
6
elif phone <=3:    print("OnePlus Nord CE4 Lite 5G price: 350000rs")

elif phone <=4:
    print("Poco X7 price: 450000rs")

elif phone <=5:
    print("i phone 16 pro price: 1,19,000rs")

else:
    print("Sorry phone are not available ")
  


#SESSION 6 — DICTIONARIES & SETS

sales= {
    "iPhone": 15900,
    "Vivo": 23990,
    "Onepules": 19000
    }
print(sales)
#Dictionary se value kaise nikalte hain?
print(sales["Vivo"])
print(sales["iPhone"])

#Value update kaise karein?
sales["iPhone"]=18900
print(sales)

#New key–value add kaise karein
sales["smartWatch"]=16666
print(sales)

sales["opoo"]= 12000
print(sales)

#Key–value delete kaise karein?
sales.pop("Vivo")
print(sales)

#REAL DATA ANALYTICS DEMO

sales = {
    "jan": 15980,
    "feb": 12970,
    "mar": 19099
    }
total= 0
for month in sales:
    total=total+sales[month]
print("Total Sales:", total)
#Dictionary important methods
print(sales.keys())
print(sales.values())
print(sales.items())

# EX-

students = {
    "Amit": 80,
    "Neha": 90,
    "Ravi": 75
    }

students["Neha"]= 95
print(students)
students["Sita"]= 88
print(students)
students.pop("Ravi")
print(students)


#EX - Practice Exercise — Dictionary

products = {
    "Mobile": 15000,
    "Laptop": 55000,
    "Tablet": 20000
}
print(products)
products["Laptop"]=60000
print(products)
products["SmartWatch"]=8000
print(products)
products.pop("Tablet")
print(products)



# SETS Set = unique values ka collection

#SET banate kaise hain

cities= {"Ahmed","Gov","Raj"}
print(cities)

#Duplicate values ka kya hota hai
num={10,22,25,10,23,22,10,30,25,10}
print(num)

#SET me value add kaise karein?
name={"JIgar","MOhit","Raju1"}
name.add("Panchal")
print(name)

#SET se value remove kaise karein
name.remove("JIgar")
print(name)

#PRACTICE
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
print(emails)
set_emails =set(emails)
print(set_emails)

set_emails.add("d@gmail.com")
print(set_emails)

set_emails.remove("b@gmail.com")
print(set_emails)


#SET OPERATIONS

#1️⃣ union() — dono sets ke saare unique elementsV

a={2,3,6}
b={4,3,5}
print(a.union(b))

#2 intersection() — common elements
print(a.intersection(b))

#3 difference() — a me jo hai, b me nahi
print(a.difference(b))

# PRACTICE---------------------

website_a_users = {"u1", "u2", "u3"}
website_b_users = {"u3", "u4", "u5"}


print(website_a_users.union(website_b_users))
print(website_a_users.intersection(website_b_users))
print(website_a_users.difference(website_b_users))
"""

customers = ["Amit", "Ravi", "Neha"]
for index, c in enumerate(customers, start=1):
    print(f"{index} Name:{c}")


# find the gst

def GST_FIND ( price , GST):
    GST_F =price * GST/100
    print(GST_F)
GST_FIND (1000 , 10)








