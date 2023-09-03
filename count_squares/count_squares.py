def main():
    string = input("Input numbers 1-3 in a sequence to see number of squares present: ")
    print("Number of squares in {}:\n{} squares".format(string, count_squares(string)))


def count_squares(s):
    num_squares = 0

    for search_group in range(1, (len(s)//2)): # Will end loop after reaching half of the length of the string, as no more matches are possible beyond this
        for i in range((len(s)//search_group)):

        # The number of iterations a search needs to go through and check an entire string will never exceed the length of the string

        # Search group number tells function how do current search
        
        # Due to slices being half-inclusive can't use signed (negative) integers in the slices as I won't be able to handle all cases the same
        # To select the last two characters I'll need to do something like [-2:], whilst other characters would be [-3:-1]
        # So instead just repeat the above but start off by +1

            for offset in range(search_group):  # 0 = no offset, search_group is the maximum possible offset before repeat
                if((((i+2)*search_group)+offset) > len(s)):
                    break
                # the addition to i represents the i value in the next iteration or one after that
                # eg: the slices are like: is 1st iteration:2nd == 2nd:3rd?
                elif(int(s[(i*search_group)+offset:((i+1)*search_group)+offset]) == int(s[((i+1)*search_group)+offset:((i+2)*search_group)+offset])):
                    num_squares += 1

    return num_squares


main()

# Process:
# select each group of 2 from start and continue till the end
# Then do again but this time starting from the end
# Increase search group to 3 and repeat

# If search group greater than half of total length break as no more squares are possible

# len(s)//search_group would give the number of possible iterations for a search_group without going out of bounds
# can update this number for offset too: len(s) - offset//search_group to avoid out of bounds