def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <operation> <num1> <num2>")
        sys.exit(1)

    operation = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    else:
        print("Invalid operation. Use 'add', 'subtract', or 'multiply'.")
        sys.exit(1)

    print(f"Result: {result}")
