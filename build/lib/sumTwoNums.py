
import argparse

# add two integers
def add_numbers(a, b):
    return a + b

def main():
    parser = argparse.ArgumentParser(description="Sum two numbers.")
    parser.add_argument('a', type=int, help="First number")
    parser.add_argument('b', type=int, help="Second number")
    
    args = parser.parse_args()
    result = add_numbers(args.a, args.b)
    print(f"The sum of {args.a} and {args.b} is {result}")

