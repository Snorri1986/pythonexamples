users = ['Dave','John','Sara']
data = ['Dave',42,True]
emptylist = []

print('Dave' in data)

print(users.index('Dave')) # returns an index of particular value

#gets range of values
print(users[0:2])
print(users[1:])

print(len(users)) # returns length of a list

# add elements to the list
users.append('Den') 
print(users)

users += ['Kisa']
print(users)

users.extend(['Kisa2','Kisa3'])
print(users)

users += 'Test'
print(users)

users.insert(0,'Bob') # add an element before index
print(users)

users[2:2] = ['Eddie','Alex']
print(users)

users.remove('Bob')
print(users)

print(users.pop()) 

#####################################################
# Sorted list with numbers
nums = [7,12,67,90,100]
print(sorted(nums,reverse=False))

# Tupels
mytuple = (('Dave',42,True))
anotherTuple = (1,4,5,6)
print(mytuple)
print(anotherTuple)

