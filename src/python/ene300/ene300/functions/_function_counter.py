from functools import wraps

def function_counter(function):
    @wraps(function)
    def increase_count(*args, **kwargs):
        increase_count.calls += 1
        return function(*args, **kwargs)
    increase_count.calls = 0
    return increase_count