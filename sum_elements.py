import sys

MAX = 100

def calculate_sum(arr: list[int]) -> int:
    return sum(arr)

def exit_with_message(message: str):
    print(message)
    sys.exit(1)

def get_integer_input(prompt: str) -> int:
    try:
        return int(input(prompt))
    except ValueError:
        exit_with_message("Invalid input. Please enter valid integers.")

def main():
    try:
        n = get_integer_input("Enter the number of elements (1-100): ")
        if not 1 <= n <= MAX:
            exit_with_message("Invalid input. Please provide a digit ranging from 1 to 100.")

        print(f"Enter {n} integers:")
        arr = [get_integer_input(f"Element {i+1}: ") for i in range(n)]

        total = calculate_sum(arr)
        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        sys.exit(1)

if __name__ == "__main__":
    main()
