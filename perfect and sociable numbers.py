def is_perfect(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    if sum(divisors) == number:
        print(f"{number} is a perfect number. Divisors: {divisors}")
    else:
        print(f"{number} is not a perfect number.")

def are_amicable(num1, num2):
    divisors_num1 = [i for i in range(1, num1) if num1 % i == 0]
    divisors_num2 = [i for i in range(1, num2) if num2 % i == 0]
    if sum(divisors_num1) == num2 and sum(divisors_num2) == num1:
        print(f"{num1} and {num2} are amicable numbers. Divisors of {num1}: {divisors_num1} (Sum: {sum(divisors_num1)}). Divisors of {num2}: {divisors_num2} (Sum: {sum(divisors_num2)})")
    else:
        print(f"{num1} and {num2} are not amicable numbers.")

def find_sociable(number, limit=10):
    sociable_numbers = []
    current = number
    for _ in range(limit):
        divisors_sum = sum([i for i in range(1, current) if current % i == 0])
        if divisors_sum == number or divisors_sum in sociable_numbers:
            sociable_numbers.append(divisors_sum)
            print(f"Sociable chain found: {sociable_numbers}")
            return
        elif divisors_sum == current or divisors_sum == 1:
            break
        else:
            sociable_numbers.append(current)
            current = divisors_sum
    print("No sociable chain was found.")
    if sociable_numbers:
        print(f"Attempted chain: {sociable_numbers}")

def main():
    print("Perfect Number Check:")
    is_perfect(28)  # Example perfect number

    print("\nAmicable Numbers Check:")
    are_amicable(220, 284)  # Example amicable pair

    print("\nSociable Numbers Check:")
    find_sociable(12496)  # Attempt to find a sociable chain

if __name__ == "__main__":
    main()
