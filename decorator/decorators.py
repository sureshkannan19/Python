from functools import wraps


def email_decorator(func):
    @wraps(func)  # to retain the docstring
    def wrapper(*args, **kwargs):
        print(f"Welcome {args}")
        func(*args, **kwargs)
        print("Bye")

    return wrapper


@email_decorator
def greetings_message(name):
    """Welcome message"""
    print("Have a nice day,")


# greetings_message = email_decorator(greetings_message)
greetings_message("SK")
print(greetings_message.__doc__)


def multiplier(n):
    def decorator(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * n

        return inner

    return decorator


@multiplier(2)
def calculate(x):
    return x


print(calculate(5))