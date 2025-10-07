def simple_decorator(func):
    def wrapper():
        print("Hello before!")
        func()  # This calls the original function
        print("Hello after!")
    return wrapper

@simple_decorator
def say_hi():
    print("Hi there!")

say_hi()