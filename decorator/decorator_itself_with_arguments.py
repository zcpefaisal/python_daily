def repeater_decorator(repeat_count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(repeat_count):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeater_decorator(repeat_count=5)
def hello():
    print("Hello !")

hello()