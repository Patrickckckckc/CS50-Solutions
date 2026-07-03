def main():
    text = input("MATH:")
    solution = interpreter(text)
    print(solution)


def interpreter(text):
    # Divided the strin into 3 parts
    x, y, z = text.split(" ")
    x = float(x)
    z = float(z)
    match y:
        case '+':
            return x + z
        case '-':
            return x - z
        case '/':
            return x / z if z != 0 else "Error: division by zero"
        case '*':
            return x * z
        case _:
            return "Unknown operator"



main()
