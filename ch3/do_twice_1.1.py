# Do twice
# demonstrates a function being passed as an argument to another function
# H@cker 08June2016

def do_twice(f,value):
    f(value)
    f(value)
    
def print_spam(x):
    print(x)

def print_twice(x):
    print(x)
    print(x)

def do_four(f,x):
    f(print_spam,x)
    f(print_spam,x)
# passing print_spam (no parameters, void function) as an argument
#modified now to include parameters, which also gets passed to the function calling function as an argument

word = input('what would you like printed four times: ')
#do_twice(print_spam,word)
#do_twice(print_twice,'spam')
do_four(do_twice,word)
