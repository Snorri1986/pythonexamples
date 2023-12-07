def hello():
    print("Hello world")

hello()

def sum(num1,num2):
    print(num1 + num2)

sum(2,3)

def sum_return(num1=0,num2=0):
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

sum_from_function = sum_return(100,3)
print(sum_from_function)

sum_from_function = sum_return()
print(sum_from_function)

# count of arguments is unknown
def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Denys","Kisa","Doggi")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="Denys",last="Doggi")