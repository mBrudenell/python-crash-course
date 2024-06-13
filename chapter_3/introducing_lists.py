#lists are a collection of items in a certain order (0-9, ABCD, e.c.t)
#[] usually indicates list.

#example list
bicycles = ['trek', 'cannondale', 'redline', 'specialized',]
print(bicycles)

#accessing items in a list using index
#first write the name of the list, followed by index in square brackets
print(bicycles[0])
#printing it title case
print(bicycles[0].title())

#REMEMBER index positions start at 0 not 1.
#to acess the last item, ask for index -1.The second last, -2 and so on. 
print(bicycles[-1])

#using individual values from a list(using an f string)
bicycles = ['trek', 'cannondale', 'redline', 'specialized',]
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#excercises
#1- printing names from a list using their index
names = ['James', 'Mhairi', 'Anne', 'Jane']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#2- creating a message to each friend, using an f string and index
message = f'Hello {names[0]}!, how are you today?'
print(message)

#3- creating a list of bands and making statements about them
bands = ['radiohead', 'muse', 'pink floyd', 'nirvanna']
message = f'my favorite band is {bands[0]}, but i enjoy {bands[2]} for background study music. I like listening to {bands[1]} for running, and {bands[3]} too!'
print(message)

#modifying, adding and removing elements
#dynamic lists are lists that you can add and remove elements from 



