from functools import wraps


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('auth wrapped called')
        return func(*args,**kwargs)
    return wrapper