# decorator are in which function acts as variables where functions can be passed to others functions and can be returned 
# also 
def announce(f) :
    def wrapper() :
        print("about to run the function ")
        f()
        print("done with the function ")
    return wrapper
@announce
def hello():
    print("hare krishna ")

hello()