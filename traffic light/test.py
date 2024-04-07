import random

min = 0
max = 10

number_of_guesses =0
secret_number = random.randint(min,max)

def get_number_from_user():
    user_guess=input(f"please inter a guess in range {min} to {max}\n")
    return user_guess

def compare(user_guess):
    if(user_guess>secret_number):
        print(f"{user_guess} is greater than the number")
    else:
        print(f"{user_guess} is smaller than the number")

#if found returns 1 else 0
def check_guess_update_counter(user_guess):
    global number_of_guesses
    #print(f"secret_number is {secret_number} and my guess is {user_guess}, number of guesses so far is {number_of_guesses}\n")
    if user_guess==secret_number:
        print("found you win!!!!")
        return 1

    compare(user_guess)

    number_of_guesses +=1
    return 0

def main():
    while not check_guess_update_counter(int(get_number_from_user())):
        True



if __name__ == "__main__":
    main()