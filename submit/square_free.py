class NegativeNumberException(Exception):
    def __init__(self):
        self.str = "Please input a postive integer"


def main():
    n = int(input("Input a positive integer: "))

    try:
        print(print3Blocks(square_free(n)))
    except NegativeNumberException as e:
        print(e.str)


def square_free(n):
    if(n < 0):
        raise NegativeNumberException    
    elif(n >= 0):
        a = "1"  # This initial value will be returned if n = 0
        count = 1
        for i in range(n):
            a = replace(a, count)  # Replaces characters in string
        return a


def replace(a, count):
    new_str = ""

    for value in a:
        # Pass in count of current element to isEven
        if(is_even(count)):  # Handles even positions
            if((int(value) == 1)):
                new_str += "321"
            elif((int(value) == 2)):
                new_str += "132"
            elif((int(value) == 3)):
                new_str += "213"
        else:  # Handles odd positions
            if((int(value) == 1)):
                new_str += "123"
            elif((int(value) == 2)):
                new_str += "231"
            elif((int(value) == 3)):
                new_str += "312"
        count += 1

    return new_str


def is_even(count):
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