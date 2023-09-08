def main():
    n = int(input("Input a positive integer: "))

    print(print3Blocks(square_free(n)))

    print("Sequence when n = 0: {}".format(print3Blocks(square_free(0))))
    print("Sequence when n = 1: {}".format(print3Blocks(square_free(1))))
    print("Sequence when n = 2: {}".format(print3Blocks(square_free(2))))
    print("Sequence when n = 3: {}".format(print3Blocks(square_free(3))))


def square_free(n):
    if(n >= 0):
        a = "1"  # Holds the output string for the current iteration
        count = 1  # Counter used to track index
        for i in range(n):
            a = replace(a, count)  # Replaces characters in string
        return a


def replace(a, count):
    new_str = ""

    for value in a:
        if(is_even(count)):  # Handles even positions if is_even() returns true
            if((int(value) == 1)):
                new_str += "321"
            elif((int(value) == 2)):
                new_str += "132"
            elif((int(value) == 3)):
                new_str += "213"
        else:  # Handles odd positions if is_even() returns false
            if((int(value) == 1)):
                new_str += "123"
            elif((int(value) == 2)):
                new_str += "231"
            elif((int(value) == 3)):
                new_str += "312"
        count += 1

    return new_str


def is_even(count):  # Checks if the mod of the index number is 0 to determine if the number is even
    if(count % 2 == 0):
        return True
    else:
        return False


def print3Blocks(s):
    spaced_blocks = ""

    for i in range(0, len(s), 3):
        spaced_blocks += (s[i:i+3] + " ")

    return spaced_blocks[:-1]  # Returns the formatted string


main()