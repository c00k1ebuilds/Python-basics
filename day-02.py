# ============================================
# DAY 02 — Type Conversion, Mad Libs & Lists
# April 22, 2026
# ============================================


# --- SECTION 1: BASIC CALCULATOR (WHOLE NUMBERS) ---

num1 = input('enter a number: ')
num2 = input('enter a number: ')
result = int(num1) + int(num2)
print(result)


# --- SECTION 2: BASIC CALCULATOR (DECIMAL NUMBERS) ---

num1 = input('enter a number: ')
num2 = input('enter a number: ')
result = float(num1) + float(num2)
print(result)


# --- SECTION 3: MAD LIBS GAME ---

color = input('enter a color: ')
plural_noun = input('enter a plural noun: ')
celebrity = input('enter a celebrity name: ')
print('roses are ' + color)
print(plural_noun + ' are blue')
print('i love ' + celebrity)


# --- SECTION 4: MY OWN MAD LIBS GAME ---

hate = input('enter the thing you hate: ')
group = input('enter a group of something: ')
youtuber = input('enter your fav youtuber: ')
print('i eat ' + hate)
print('i love to play with ' + group)
print(youtuber + ' is cool')


# --- SECTION 5: LISTS ---

# basic list — accessing by index
friends = ['kevin', 'karen', 'jim']
print(friends[2])
# lists store large amounts of data in one variable
# index starts at 0, negative index (-1) accesses from the back

# accessing portions of a list using slicing
friends = ['kevin', 'karen', 'jim', 'cookie', 'sammy', 'chai']
print(friends[1:])
# friends[1:] prints everything from index 1 to the end

print(friends[1:4])
# friends[1:4] prints index 1, 2, 3 — last index (4) is excluded
# so output is: karen, jim, cookie — sammy is NOT included

# modifying a list element
friends = ['kevin', 'karen', 'jim', 'cookie', 'sammy', 'chai']
friends[1] = 'mike'
print(friends[1])
# we replaced karen with mike at index 1
