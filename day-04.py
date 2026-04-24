# ============================================
# DAY 04 — Full Revision of Everything So Far
# April 24, 2026
# ============================================

# --- PRINT ---
print("mission: become an ml engineer")
print("day 4. still here.")

# --- VARIABLES & DATA TYPES ---
name = "cookie"
age = 18
gpa = 9.2
is_learning = True
print(name, age, gpa, is_learning)
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_learning))

# --- STRING FUNCTIONS ---
phrase = "aspiring ml engineer"
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
print(phrase.islower())
print(len(phrase))
print(phrase[0])
print(phrase.index("ml"))
print(phrase.replace("ml", "ai/ml"))
print(phrase + " · building from zero")

# --- ESCAPE CHARACTERS ---
print("she said \"keep going\"")
print("day 1\nday 2\nday 3\nday 4")

# --- NUMBERS & ARITHMETIC ---
print(10 + 5)
print(10 - 3)
print(4 * 6)
print(15 / 4)
print(10 % 3)
print(2 ** 8)

# --- MATH MODULE ---
from math import *
print(floor(4.9))
print(ceil(4.1))
print(sqrt(144))
print(abs(-99))
print(pow(2, 10))
print(max(5, 9, 3))
print(min(5, 9, 3))
print(round(3.7))

# --- TYPE CONVERSION ---
num = "25"
print(int(num) + 5)
print(float(num) + 0.5)
print(str(100) + " days of code")

# --- USER INPUT ---
name = input("enter your name: ")
age = input("enter your age: ")
print("hello " + name + " you are " + age + " years old")

# --- CALCULATOR ---
num1 = input("enter a number: ")
num2 = input("enter a number: ")
print("sum:", float(num1) + float(num2))
print("difference:", float(num1) - float(num2))
print("product:", float(num1) * float(num2))
print("division:", float(num1) / float(num2))

# --- MAD LIBS ---
color = input("enter a color: ")
noun = input("enter a noun: ")
celeb = input("enter a celebrity: ")
print("roses are " + color)
print(noun + " are blue")
print("i love " + celeb)

# --- LISTS ---
skills = ["python", "git", "github", "math", "ai/ml"]
print(skills)
print(skills[0])
print(skills[-1])
print(skills[1:4])
skills[0] = "python basics"
print(skills)

friends = ["kevin", "karen", "jim", "cookie", "sammy"]
print(friends[1:])
print(friends[:3])
print(friends[-1])
friends[1] = "mike"
print(friends)
