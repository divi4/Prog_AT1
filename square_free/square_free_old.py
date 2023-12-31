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
        for i in range(n):
            a = replace(a) # Replace characters in string
        return a


def replace(a):
    new_str = ""
    for count in range(len(a)):
        # Pass in index of current element to isEven
        if(count % 2 == 0): # Handles even positions
            for count in range(len(a)):
                if((int(a[count:count+1]) == 1)):
                    new_str += "321"
                elif((int(a[count:count+1]) == 2)):
                    new_str += "132"
                elif((int(a[count:count+1]) == 3)):
                    new_str += "213"
        # TODO: consider if better to use elif instead
        else: # Handles odd positions
            for count in range(len(a)):
                if((int(a[count:count+1]) == 1)):
                    new_str += "123"
                elif((int(a[count:count+1]) == 2)):
                    new_str += "231"
                elif((int(a[count:count+1]) == 3)):
                    new_str += "312"
    return new_str


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