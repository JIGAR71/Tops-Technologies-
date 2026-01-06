

#SESSION 9 — FUNCTIONS (def, arguments, return)
"""
Function kya hota hai?

Function = ek kaam ko naam de dena, taaki baar-baar use ho sake

Real life:

Calculator me Add button

Phone me Call button

Python me:

Ek baar logic likho

Jitni baar chaho use karo

Function kyun use karte hain?

Code repeat nahi hota

Code clean & readable hota hai

Bug fix easy hota hai

Analytics projects me must hai

     FUNCTION SYNTAX
  def function_name():
     code

"""

#Example

def greet():
    print("Hello Jigar")
greet()


#FUNCTION with ARGUMENT (INPUT lena)

def greet(name):
    print("Name",name) # yaha jo print me hamne "Name liya hai vo niche greet ke aage lag jayega yani ki Name jigar output ayega ye function ba gaya "

greet("Jigar")
greet("Amit")



#REAL DATA ANALYTICS EXAMPLE

def caluation_discount(price,rate):   #yaha par hamne jo function banaya hai caluation_discount kar ke usme hamne price and rate rak diya ab last me ham
    discount = (price*rate)/100       # jab value ko dalnege to vo function ke hiab se value dedega bar bar hame code nhi likhna hoga 
    final_d = price- discount
    print(final_d)


caluation_discount(10000,10)
caluation_discount(5300,5)


#FUNCTION with return (VERY IMPORTANT) -- (print sirf dikhata hai) -- (return value wapas deta hai)

def c_d(price,rate):
    dcount= (price*rate)/100
    return dcount, price-dcount

d = c_d (1500,10)
print(d)


#Multiple arguments

def total_price(price,gst):
    gst_find= (price*gst)/100
    return price+gst_find
final_amout = total_price(1000,10)
print(final_amout)


#Function reuse (power samjho)

prices = [1000, 2000, 3000]
def add_gst(price):
    return price*0.10

for p in prices:
    print(add_gst(p))




#PRACTICE

# Q.1

def square(n):
    return n*n
rusult = square(6)
print(rusult)


# Q.2
def check_even(n):
    if n % 2 ==0:
        return "even"
    else:
        return "odd"
rusult = check_even (7)
print(rusult)


# Q.3
def add(a, b):
    return a+b
result=add(13,7)
print(result)


# Q.4
def find_max(a, b):
    if a>b:
        return a
    else:
        return b
result = find_max(12,33)
print(result)











































































