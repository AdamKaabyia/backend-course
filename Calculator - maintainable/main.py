from calcolator import Calculator
import sys

if __name__ == "__main__":
    calc = Calculator()
    num1 = input("number 1:")
    num2 = input("number 2:")
    operator = input("operator:")
    print(calc.calculate(num1, num2, operator))
