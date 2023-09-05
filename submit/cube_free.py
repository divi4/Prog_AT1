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
            t = t + find_inverse(t)  # Concatenates the current string with its inverse to create a new string
        return t


def find_inverse(t):  # Inverses the passed string
    inverse = ""
    for count in range(len(t)):  # Compares characters in string to a conditional to return its inverse
        if(int(t[count:count+1]) == 0):
            inverse += "1"
        else:
            inverse += "0"
    return inverse


main()