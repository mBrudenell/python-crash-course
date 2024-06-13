#ending files in .py indicates that it is a python file.World is a variable and is connected to value "hello_world.py"
world = "hello_world.py"
print(world)

#strings - a series of characters within quotes 
"this is a string"

#changing case of a string - the title() is an action, and the . tells python to act on the variable name 
name = "james plant"
print(name.title())

#changing a string to all upper and lower case
name = "james plant"
print(name.upper())
print(name.lower())

#using variables in strings using f string - using f before the quotation marks, tells python to replace each variable with its value 
first_name = "james"
last_name = "plant"
full_name = f"{first_name} {last_name}"
print(full_name)

#composing messages using f strings 
message = f"Hello, {full_name.title()}"
print(message)

#adding whitespace 
# \t adds a tab to your text
#\n adds a new line

#stripping whitespace using rstrip(). This only temporarily removes the whitespace, and when called again without rstrip(), it will return
my_name = 'Mhairi '
print(my_name)
print(my_name.rstrip())
print(my_name)

#To remove whitespace permanently, you just assign the stripped value to the variable name
my_name = 'Mhairi '
my_name = my_name.rstrip()
my_name

#you can also use strip(), to strip from both sides, or lstrip to remove from the left side
my_name = '  Mhairi  '
my_name.lstrip() 

#Removing prefixes (such as https at the beggining of a URL)
met_office_url = 'https://www.metoffice.gov.uk/'
met_office_url.removeprefix('https://')

#This is again temporary, and to make it permanent, you can assign it to a new variable 
met_office_url = 'https://www.metoffice.gov.uk/'
met_office_without_prefix = met_office_url.removeprefix('https://')
print(met_office_without_prefix)

#Excercises
#1-using f string to print a message 
name = 'Eric'
message = f'Hello {name} , would you like to learn some python today?'
print(message) 

#2-printing a name in lower and upper case
name = 'mhairi'
print(name.upper())
print(name.lower())

#3-printing a message, using two f strings
author = 'Carl Sagan'
quote = '"It is far better to grasp the universe as it really is than to persist in delusion, however satisfying and reassuring."'
message = f'{author} once said, {quote}.'
print(message)

#4-using strip()
name = "Carl Sagan      "

print(name.strip())

#5-removing suffixes
filename = 'python_notes.txt'
filename_new = filename.removesuffix('.txt')
print(filename_new)

#numbers(integers)
2 + 3 # = 5
3 - 2
2 * 8
3 / 2
3 / 2 * 8
2 + 4 / 6

#numbers(floats)
#any number with a decimal point
0.1 + 0.2 # = 0.2
0.2 * 8.0
20.2 / 0.8
0.8 - 2.2

#numbers(integers and floats)
#when dividing 2 numbers, even if they're integers that result in a whole number, you'll always get a float
4 / 2 # = 2.0 
#this is the same when mixing integers and floats - you will get a float 
1 + 2.0 # = 3.0 
3.0 ** 2 # = 9.0

#underscores in numbers
#this can make longer numbers more readable( this is not shown when printed out)
universe_age = 14_000_000_000 # = 14000000000

#multiple assignment(assigning values to more than one variable)
x, y, z = 0, 0, 0
#make sure that the variables match the variable values, and in order you want to assign them 

#constants(variable that stays the same throughout the programm, we simply use capital letters)
MAX_CONNECTIONS = 5000

#excercises
#1- Number eight
print(5+3)
print(16/2)
print(4*2)
print(16-8)

#2- Favorite number
fave_number = 8
message = f'My favorite number is {fave_number}!'
print(message)


