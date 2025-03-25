def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    choice = input("Ingrese su elección (1/2/3/4): ")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if choice == '1':
        print(f"Resultado: {add(num1, num2)}")
    elif choice == '2':
        print(f"Resultado: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Resultado: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Resultado: {divide(num1, num2)}")
    else:
        print("Opción inválida")

if __name__ == "__main__":
    calculator()