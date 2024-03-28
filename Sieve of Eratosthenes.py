def sieve_of_eratosthenes(max_num):
    prime = [True for _ in range(max_num + 1)]
    p = 2
    while p * p <= max_num:
        if prime[p]:
            for i in range(p * p, max_num + 1, p):
                prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, max_num + 1) if prime[p]]
    return prime_numbers


max_num = 150
prime_numbers = sieve_of_eratosthenes(max_num)
print(f"Prime numbers up to {max_num}:", prime_numbers)
