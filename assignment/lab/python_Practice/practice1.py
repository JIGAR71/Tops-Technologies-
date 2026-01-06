"""
1.#print
print("hellow jigar")


2. # this is single line comment
"""  """

3. #Variable

a=10
b=20
c=a+b
print(c)

print("\n")

# Arithmetic Operators 

# Variables
a = 15
b = 4

# Addition (+)
add = a + b
print( add)

# Subtraction (-)
sub = a - b
print(sub)

# Multiplication (*)
mul = a * b
print( mul)

# Division (/)
div = a / b
print(div)

print("\n")
# Assignment Operators in Python

x = 10
print(x)

x = 5
print( x)

x += 3
print(x)

x -= 2  
print(x)

x *= 4 
print(x)

x /= 2 
print(x)

print("\n")
# Comparison Operators in Python

a = 10
b = 5

print( a == b)

print(a > b)    

print( a < b)     

print(a >= b)  

print(a <= b)

print("\n")
# Logical Operators in Python

a = 10
b = 5

print( a > 5 and b < 10)   
print( a > 15 and b < 10) 

print( a > 5 or b > 10)    
print( a < 5 or b > 10)     

print(not (a > 5))             
print(not (b > 10))          



#4 types of collection

#list

# Normal list
my_list = ["jigar", "Raj", "Kamal", "Yesh", "Vinod"]
print(my_list)

print("\n")

# Print any one value in list

my_list = ["apple","bananaa","cherry","mongo","Ornge"]
print(my_list[2])

print("\n")

#print all value in list

my_list = ["apple","bananaa","cherry","mongo","Ornge"]
print(my_list[0:])

print("\n")

#print a any 3 value

my_list = ["apple","bananaa","cherry","mongo","Ornge"]
print(my_list[1:3])

print("\n")

# add a New element
my_list = ["apple","bananaa","cherry","mongo","Ornge"]
my_list.append("Garjar")
print(my_list)

print("\n")
# remove a any one

my_list = ["raj","kalpesh","yesh","kamlesh","jigar","raj","vansh"]
my_list.remove("raj")
print(my_list)

print("\n")

# 2 Tuple
my_tuple = ("Banana","Apple","cherry","Gajar")
print(my_tuple)

my_tuple = ("Banana","Apple","cherry","Gajar")
print(my_tuple[3])

my_tuple = ("Banana","Apple","cherry","Gajar")
print(my_tuple[0:3])

print("\n")


#3 set
my_set = {"apple","bananaa","cherry","mongo","Ornge"}
print(my_set)

my_set = {"apple","bananaa","cherry","mongo","Ornge"}
my_set.add("Gajar")
print(my_set)

#update
my_set = {"apple","bananaa","cherry","mongo","Ornge"}
my_set.update(["Gajar","Muli","Kiwi"])
print(my_set)

#Dictionary

print("\n")

#odd aand evan

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")



balance = 5000  # starting balance
amt = int(input("Enter amount to withdraw: "))

if amt <= balance:
    balance = balance - amt
    print("Please collect ", amt)
    print("Carent Balance:", balance)
else:
    print("Amouunt are saccessefuly withdraw balance!")



# grading system
marks = int(input("Enter your Marks "))
    
if marks >= 90:
    print("Grad: A1");
    
elif marks >= 80:
    print("Graed: A")
    
elif marks >= 70:
    print("Grad: B")

elif marks >= 60:
    print("Grad: C")

elif marks >= 50:
    
    print("Grad: D")
    
else:
    print("Fail")



#loop

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print("Main kha raha hun",fruit)


fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print("Main kha raha hun", (fruits[0]))



for i in range(5, 0, -1):       
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  


for i in range(1,20):
     for j in range(1, i+1):
         print(j, end=" ")
     print()
"""
# printing numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)
    
# print each character for the string "HELLO" using a for loop
for char in "HELLO":
    print(char)
    
#print the square of numbers from 1 to 5 using a for loop
for i in range(1, 6):
    print(1 * i)
      
# use a for loop to print only even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)     

#Given a list of numbers, print each fruit in the list using a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)   

# printing numbers from 10 to 1 in revers using a for loop and range
for i in range(10, 0, -1):
    print(i)
 
# given a list of num = [3, 4, 9, 12, 15, 20] print each number in the list using a for loop
num = [3, 4, 9, 12, 15, 20]
for number in num:
    print(number)    

#print the multiplication table of 6 using a for loop
for i in range(1, 11):
    print("6 x", i, "=", 6 * i)
 
#write a for loop to count how many vowels are in the string "Python Programming"
text = "Python Programming"
vowel_count = 0
for char in text:
    if char.lower() in 'aeiou':
        vowel_count += 1
print("Number of vowels:", vowel_count)
               
            