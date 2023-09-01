# Follow pep style guidelines

class NegativeNumberException(Exception):
    def __init__(self):
        self.str = "Please input a postive integer"


def main():
    n = int(input("Input a positive integer: "))

    try:
        print(thue_morse(n))
    except NegativeNumberException as e:
        print(e.str)


def thue_morse(n):
    if(n < 0):
        raise NegativeNumberException    
    elif(n >= 0):
        t = "0"
        for i in range(n):
            t = t + xor(t) # Need to inverse the second half of string
        return t


def xor(t):
    # Go through t string one by one and swap each char for opposite character
    q = 1
    inverse = ""
    for count in range(len(t)):
        if((int(t[count:count+1]) and not q) or (not int(t[count:count+1]) and q)):
            inverse += "1"
        else:
            inverse += "0"
    return inverse

main()
