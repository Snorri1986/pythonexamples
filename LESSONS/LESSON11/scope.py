

name = "Dave" # global scope


    
greeting("Denys")

def another():
    color = "blue"
    def greeting(name):
        color = "blue"
        print(color)
        print(name) # print the variable from local scope 

another()

