#String data types
#Litteraly assignment
first = 'Dave'
last = 'Gray'

print(type(first))
print(type(last))

print(type(first) == str)
print(isinstance(first,str))

#construction function
pizza = str("Peperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza,str))

#Casting a number to string
decade = str(1980)
print(type(decade))

music = "I like the music from " + decade + "s."
print(music)

#---------------------------------------------------------
#String methods
print(first)
print(first.lower())
print(first.upper())
print(first)

multiline = '''
Hey peoples! You are so cool!
'''

print(multiline.title())
print(multiline.replace('so','extremly'))


print(len(multiline))
multiline += "                                         "
multiline = "             " + multiline
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

#Print a menu
title = "menu".upper()
print(title.center(20,'=')) # ==========MENU==========
print("Coffee".ljust(16,'.') + "1$".rjust(4)) # Coffee..........  1$
print("Muffin".ljust(16,'.') + "2$".rjust(4)) # Muffin..........  2$
print("Cheescake".ljust(16,'.') + "4$".rjust(4)) # Cheescake..........  4$

print("")

print(first[1])
print(first[-1])
print(first[1:]) # ave. Range

# Methods which return booleans
print(first.startswith('D'))
print(first.endswith('e'))

#---------------------------------------------------------
# Boolean data type

myvalue = True
x = bool(True)
print(type(x))

#---------------------------------------------------------
# Numeric data types
price = 100
best_price = int(80)
print(type(price))
print(type(price) == int)
print(isinstance(price,int))

