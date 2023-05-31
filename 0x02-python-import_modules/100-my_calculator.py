#!/usr/bin/python3

if __name__ == "__main__":
    import sys

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

operator = sys.argv[2]

if operator not in ['+', '-', '*', '/']:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])

if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
else:
    result = a / b

equation = f"{a} {operator} {b} = {result}"
print(equation)
