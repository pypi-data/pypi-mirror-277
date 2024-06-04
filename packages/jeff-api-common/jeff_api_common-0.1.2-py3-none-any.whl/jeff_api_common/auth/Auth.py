

def auth(func):
    def _wrrapped(*args, **kwargs):
        print("auth")