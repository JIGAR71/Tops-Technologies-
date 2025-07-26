# Module 7 - Introduction to Python

# 1) What are the types of Applications?
"""
applications is everywhere – some run on our phones, some on computers,
and some silently in the background. These include:
- Web apps (like Gmail and YouTube)
- Desktop apps (like MS Word and Excel)
- Mobile apps (like WhatsApp and Instagram)
- Games (like PUBG and Candy Crush)
- AI/ML apps (like ChatGPT )
Python helps build all of these. end this is a truly  versatile and powerful language.
"""

# 2) What is programming?
"""
Programming is basically telling the computer what to do, using a special language it understands.
Just like we use English or Hindi to communicate, computers follow instructions through code.
You can ask the computer to add numbers, display messages, save data – all using programs.
"""

# 3) What is Python?
"""
Python is a beginner-friendly and powerful programming language.
Its syntax is very clean and almost like English, which makes it easy to learn.
People use Python for building websites, automating tasks, creating AI models,
and analyzing large sets of data. It’s one of the most popular languages today.
"""

# 4) Check if a number is Positive, Negative or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# 5) Find Factorial of a Number
num = int(input("Enter a number for factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial is:", fact)

# 6) Fibonacci Series of a Given Range
n = int(input("Enter the number of Fibonacci terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 7) How does Python manage memory?
"""
The best part about Python is that it handles memory automatically.
It uses a built-in garbage collector that removes unused variables and frees up space.
So you can focus on writing code, and Python will manage memory in the background.
"""

# 8) What is the 'continue' statement?
"""
The 'continue' statement is used inside loops to skip a particular step and move to the next one.
For example, if you're looping through numbers but want to ignore even ones,
'continue' can help you skip them.
"""

# 9) Swap Two Numbers (With and Without Temp)

# With temp
a = 5
b = 10
temp = a
a = b
b = temp
print("With temp swap: a =", a, ", b =", b)

# Without temp
a, b = 5, 10
a = a + b
b = a - b
a = a - b
print("Without temp swap: a =", a, ", b =", b)

# 10) Check Even or Odd Number
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
