# A refactored version of the program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases.

MAX = 100

def calculate_sum(arr):
    return sum(arr)

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    try:
        n = get_integer(f"Enter the number of elements (1-{MAX}): ")
        if not 1 <= n <= MAX:
            print(f"Invalid input. Please provide a number from 1 to {MAX}.")
            return

        arr = []
        print(f"Enter {n} integers:")
        for i in range(n):
            arr.append(get_integer(f"Element {i+1}: "))

        total = calculate_sum(arr)
        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
