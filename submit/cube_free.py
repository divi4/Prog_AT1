def main():
    n = int(input("Input a positive integer: "))
    print(thue_morse(n))

    print("Sequence when n = 0: {}".format(thue_morse(0)))
    print("Sequence when n = 1: {}".format(thue_morse(1)))
    print("Sequence when n = 2: {}".format(thue_morse(2)))
    print("Sequence when n = 3: {}".format(thue_morse(3)))


def thue_morse(n):
    if(n >= 0):
        t = "0"  # Holds the output string for the current iteration
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