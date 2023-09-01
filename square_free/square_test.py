# Follow pep style guidelines

class NegativeNumberException(Exception):
    def __init__(self):
        self.str = "Please input a postive integer"


def main():
    n = int(input("Input a positive integer: "))

    try:
        print(square_free(n))
    except NegativeNumberException as e:
        print(e.str)


def square_free(n):
    if(n < 0):
        raise NegativeNumberException    
    elif(n >= 0):
        a = "1"  # This is returned if n = 0
        count = 1
        for i in range(n):
            a, count = replace(a, count) # Replace characters in string
            print(a)
        return a


# Just need 0 for even and 1 for odd in the isEven, don't need actual index just the pattern
def replace(a, count):
    new_str = ""
    for index, value in enumerate(list(a)):
        print('Index: {} - Value: {}'.format(count, value))
        # Pass in index of current element to isEven
        if(isEven(count)): # Handles even positions
            if((int(value) == 1)):
                new_str += "321"
            elif((int(value) == 2)):
                new_str += "132"
            elif((int(value) == 3)):
                new_str += "213"
        # TODO: consider if better to use elif instead
        else: # Handles odd positions
            if((int(value) == 1)):
                new_str += "123"
            elif((int(value) == 2)):
                new_str += "231"
            elif((int(value) == 3)):
                new_str += "312"
        count += 1
    return new_str, count


def isEven(count):
    if(count % 2 == 0):
        return True
    else:
        return False
    

main()




# How works:s
# So the next loop replaces the numbers in string created in previous loop
# Loop 1: 1
# Loop 2: 1 is replaced with 123 as in odd position so: 123
# Loop 3: 1 is replaced with 123, 2 with 132, 3 with 312 


# Pattern:
# The numbers we replace with push by 1 to the right
# from 3 to 1 in odd, starting at 312
# And 1 to 3 starting at 321 


# Length of sequence is 3^n