class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Something is happening before the class is called.")
        self.func()
        print("Something is happening after the function is called.")

@MyDecorator
def say_hello():
    print("Hello!")

say_hello()

