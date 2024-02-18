import string
import math


def is_prime(n):
    if n < 2:
        return 'NO'
    i = 2
    while i * i <= n:
        if n % i == 0:
            return 'NO'
        i += 1
    return 'YES'


key=input("what would like to do(insert the number coreesponding to the action)\n"
          "1.print the abc in uppercase or lowercase\n"
          "2.print a word starting with a specific letter\n"
          "3.print N*N multiplication table\n"
          "4.print square number of a given number\n"
          "5.check if a given number is prime\n")

match key:
    case '1':
        LowOrHigh=input("would you like them in upper or lower case?(0 is for low / 1 is for high)"
                        "\n")
        if(LowOrHigh==0):
            lower = list(string.ascii_lowercase)
            print(lower)
        else:
            upper = list(string.ascii_uppercase)
            print(upper)
    case '2':
        words=['apple','black','cave','damp','example','fish','Grape','House','Ice','Jelly','Kangaroo','Lemon','Moon','Notebook','Orange','Penguin','Quilt','Rain','Sun','Tiger','Umbrella','Violin','Watermelon','Xylophone','Yellow','Zebra']
        firtLetter = input("which letter would you like the word to start with?\n")
        res = [idx for idx in words if idx[0].lower() == firtLetter.lower()]
        print(res)
    case '3':
        N = input("insert an N please?"
                          "\n")
        N=int(N)
        for i in range(1,N+1):
            x=''
            for j in range (1,N+1):
                val=str(i*j)
                x=x + val +' '
            print(x+"\n")


    case '4':
        x = input("insert value youd like to square\n")
        print(int(x)*int(x))

    case '5':
        x = input("which number would you like to check if its a prime\n")
        print(is_prime(int(x)))
