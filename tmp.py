import random

d = 'O'

"""

"""
def ib(s):
    b = []
    for _ in range(s):
        r = []
        for _ in range(s):
            r.append(d)
        b.append(r)
    return b


def pb(b):
    for r in b:
        print(" ".join(r))


def ps(b, z):
    d = random.choice(['h', 'v'])
    s = len(b)

    if d == 'h':
        r = random.randint(0, s - 1)
        c = random.randint(0, s - z)

        for i in range(z):
            b[r][c + i] = 'S'

    else:
        r = random.randint(0, s - z)
        c = random.randint(0, s - 1)

        for i in range(z):
            b[r + i][c] = 'S'


def gug(s):
    while True:
        try:
            g = int(input(f"Enter a guess (0 to {s - 1}): "))
            if 0 <= g < s:
                return g
            else:
                print("Invalid input. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def pbp(s, n):
    b = ib(s)

    for _ in range(n):
        ps(b, random.randint(2, 4))

    pb(b)

    for _ in range(10):
        gr = gug(s)
        gc = gug(s)

        if b[gr][gc] == 'S':
            b[gr][gc] = 'X'
        else:
            pass
        pb(b)

        if all('S' not in r for r in b):
            break

    print("Game over. Thanks for playing!")


if __name__ == "__main__":
    pbp(5, 3)