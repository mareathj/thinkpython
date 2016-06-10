# Do twice
# demonstrates a function being passed as an argument to another function
# H@cker 08June2016

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')
    
# passing print_spam (no parameters, void function) as an argument
do_twice(print_spam)
