
def clock_pin_decorator(clock_pin):
    def inner_decorator(func):
        def wrapper():
            return func(clock_pin)
        return wrapper
    return inner_decorator