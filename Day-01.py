# ============================================
# DAY 01 — Python Basics
# April 19-20, 2026
# ============================================


# --- SECTION 1: PRINT & SHAPES ---

print('   /|')
print('  / |')
print(' /  |')
print('/___|')


# --- SECTION 2: STRINGS & VARIABLES ---

print('there once was a man named george,')
print('he was 70 years old.')
print('he really liked the name george,')
print('but didnt liked being 70.')

character_name='george'
character_age='70'
print('there once was a man named ' + character_name + ',')
print('he was ' + character_age + ' years old.')
print('he really liked the name ' + character_name + ',')
print('but didnt liked being ' + character_age + '.')

character_name='george'
character_age='70'
print('there once was a man named ' + character_name + ',')
print('he was ' + character_age + ' years old.')

character_name='john'
character_age='35'
print('he really liked the name ' + character_name + ',')
print('but didnt liked being ' + character_age + '.')


# --- SECTION 3: STRING FUNCTIONS ---

#we can use variable for string too
phrase='girrafe academy'
print(phrase)

#we use concatenation for joining or linking 2 strings or data or more
print(phrase + ' is cool')

# functions are little block of code which we run and it performs a specific operation for us.
# we use functions to modify our strings or get information about our strings

# this function gives lower case alphabets
print(phrase.lower())

# this function gives upper case alphabets
print(phrase.upper())

# this function helps to recognise if the string is in upper or lower case
print(phrase.isupper())
print(phrase.islower())

# we can use 2 functions together like this
print(phrase.upper().isupper())

# we use this to find the length of the string
print(len(phrase))

# we use this function to get individual character always start with 0 for first character
print(phrase[0])

# it tells us where a specific character or string is located
print(phrase.index('g'))

# we can give it two values so that it replaces the first letter with the second one
print(phrase.replace('girrafe', 'elephant'))


# --- SECTION 4: ESCAPE CHARACTERS ---

# for writing in diff line we use \n
print('girrafe\nacademy')

# for quotation marks in string we use \"
print('girrafe\"academy')

# for just a back slash we use \
print('girrafe\academy')


# --- SECTION 5: NUMBERS & ARITHMETIC ---

print(2)
print(9.0)
print(-78)
print(6+8.9)
print(7-4)
print(7*9)
print(8/2)

print(6+7*8)
print(6+(7*4))

# modulus operator
print(10%3)

# using it as variable
my_num = 58
print(my_num)

# convert no to string
print(str(my_num))
print(str(my_num) + ' is my fav number')


# --- SECTION 6: BUILT-IN MATH FUNCTIONS ---

# abs (absolute value)
my_num = -5
print(abs(my_num))

# pow (it allows us to pass 2 piece of info like first is no and second is power, like 3's square)
print(pow(3, 2))

# max (its gonna return the larger of 2 numbers that we pass into it) and min (opp of max)
print(max(6, 9))
print(min(8, 17))

# round (helps us to round a number)
print(round(3.9))


# --- SECTION 7: MATH MODULE ---

from math import *
# this math is known as math module

# floor method it will grab the lowest number
my_num = -5
print(floor(3.7))

# ceil function will do opp of floor
print(ceil(3.7))

# square root it just returns the square root of a number
print(sqrt(36))


# --- SECTION 8: USER INPUT ---

# to store whatever the user inputted into our program we make it a variable
name = input('enter ur name: ')
age = input('enter ur age: ')
print('hello ' + name + '! you are ' + age)
