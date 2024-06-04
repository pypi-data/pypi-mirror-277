from functools import wraps


def auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('wrapped called')
    return f