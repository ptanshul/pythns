def my_decorator(func):
    def wrappe1r():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrappe1r

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
