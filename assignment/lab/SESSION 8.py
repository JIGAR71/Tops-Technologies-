

#SESSION 8 — LOOPS (for, while, break, continue)

"""
Loop kya hota hai?

Ek kaam ko baar-baar repeat karna

Real life:

Sales list ka total nikalna

Customers ke naam print karna

Data rows process karna
"""

#for LOOP (MOST USED)

products = ["Apple","Banana","Kiwi"]
for p in products :
    print(p)

#Example

Phone = ["iPhone","Vivo","onepules"]
for p in Phone:
    print(p)

#range() ke saath for loop

for i in range (1,5):
    print(i)




#REAL DATA ANALYTICS EXAMPLE

sales = [1200, 3400, 5600]
total = 0

for s in sales:
    total= total+s
print(total)


#EX

fiv_daysale= [1201,3320,1232,1223,4332]
total = 0
for f in fiv_daysale:
    total= total+f
print(f)



#while LOOP

i = 1
while i <= 5:
    print(i)
    i=i+1



#break — loop todna

for i in range(1,6):
    if i == 4: # yaha hamne 4 par break laha liya lekin hamne range 1,6 tak ki di thi par print 1 se 3 tak hogi kyu ki break lagaya tha 4 par 
        break
    print(i)




#continue — current step skip karna

for i in range(1,6):
    if i ==4:
        continue # yaha Continue 4 ko remov kar dega and baki ki valu cantinue rakhega 
    print(i)

#REAL ANALYTICS EXAMPLE

sales = [1200, 0, 3400, 5600]

for s in sales:
    if s == 0:
        continue
    print(s)



#PRACTICE 1

nums = [5, 10, 15, 20]

for n in nums:
    print(n)


#2

for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)

 
# 3
prices = [100, 200, 0, 300, 0, 400]

for p in prices:
    if p == 0:
        continue
    print(p)



for i in range(1,6):
    if i % 2 != 0:
        print(i)






# zip() FUNCTION ---- zip() multiple lists ko ek saath loop karne ke kaam aata hai (,Student name + marks -- ,Product + price -- ,Month + sales)

Name= ["Jigar","Richa"]
mark =[89,94]

for n,m in zip(Name,mark):
    print(n,m)


#BASIC EXAMPLE

names = ["Amit", "Neha", "Ravi"]
marks = [80, 90, 75]

for n,m in zip(names,marks):
    print(n,m)


#DIFFERENT LENGTH LISTS (IMPORTANT)

names = ["Amit", "Neha"]
marks = [80, 90, 75] #zip() shortest list pe ruk jata hai jese isme names 2 hai and marks 3 to jitni value mil rahi thi vaha tak print kiya and fir vo satop ho gayi

for n,m in zip(names,marks):
    print(n,m)

#zip() shortest list pe ruk jata hai

products = ["Mobile", "Laptop", "Tablet"]
prices = [15000, 55000, 20000]

for p,pr in zip(products,prices):
    print(f"Products is {p} Prices is {pr}")


#zip() + list() (Advanced but useful)

a = [10,22,32]
b= [23,44,12]

z = list(zip(a,b))
print(z)


#PRACTICE

# Q.1

students = ["Amit", "Neha", "Ravi"]
scores = [70, 85, 90]

for s,sc in zip(students,scores):
    print(f"{s} scores {sc}")

# Q.2

months = ["Jan", "Feb", "Mar"]
sales = [12000, 15000, 18000]
total = 0

for m,s in zip(months,sales):
    total=total+s

print(f"Total Sales:{total}")









for i in range(1,20):
     for j in range(1, i+1):
         print(j, end=" ")
     print()

























