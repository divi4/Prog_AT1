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
            t = t + xor(t)
            # Need to inverse the second half of string, go through one by one and swap for opposite character
        return t

# Could we just make the string into a list and then find all 0s and 1s and swap them? Think more efficient TODO: test it

# Can do a XOR operation on the string to return inverse
# If not AND then must be XOR?


def inverse(t, n):
    for count in range(n):  # TODO alter hardcode
        if(t[count:count + 1] == "0"):
            return "1"
        elif(t[count:count + 1] == "1"):
            return "0"


def xor(t):
    q = 1
    inverse = ""
    for count in range(len(t)):
        if((int(t[count:count+1]) and not q) or (not int(t[count:count+1]) and q)):
            inverse += "1"
        else:
            inverse += "0"
    return inverse

main()
