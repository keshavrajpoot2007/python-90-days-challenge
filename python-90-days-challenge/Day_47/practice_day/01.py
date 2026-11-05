def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_action
def add(a, b):
    return a + b    

@log_action
def create_profile(name, role="User"):
    return {"name": name, "role": role}

add(5, 3)