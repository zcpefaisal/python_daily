def smart_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calculating...")
        result = func(*args, **kwargs)  # Passes arguments through
        print("Done!")
        return result
    return wrapper

@smart_decorator
def add(a, b):
    return a + b

print(add(2, 3))