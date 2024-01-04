

name = "Dave" # global scope
count = 1


    
#greeting("Denys")

def another():
    color = "blue"
    global count
    count += 1
    print(count)
    
    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name) # print the variable from local scope 

another()

