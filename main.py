def hello(name):
    """Say hello to someone."""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

if __name__ == "__main__":
    print(hello("World"))
    print(f"1 + 2 = {add(1, 2)}")
    print(f"3 * 4 = {multiply(3, 4)}")
