def hello(name):
    """Say hello to someone."""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    print(hello("World"))
    print(f"1 + 2 = {add(1, 2)}")
