def add_sub_div_mul(num1, num2,sign):
        match sign:
            case '+':
                return num1 + num2
            case '/':
                if num2 == 0:
                    raise ZeroDivisionError("Division by zero is undefined")
                return num1 / num2
            case '*':
                return num1 * num2
            case '-':
                return num1 - num2
            case _:
                raise ValueError(f"Unsupported operation: {sign}")

