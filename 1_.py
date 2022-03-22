
def lower_case(func):
    def wrapper():
        # execute code before
        result = func()
        return result
        # execute code after 
    return wrapper