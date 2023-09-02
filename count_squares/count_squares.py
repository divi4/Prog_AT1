def count_squares(s):
    num_squares = 0

    for search_group in range(2, (len(s)//2)+1): # Will end loop after reaching half of the length of the string, as no more matches are possible beyond this
        for i in range(len(s)): # The number of iterations a search needs to go through and check an entire string will never exceed the length of the string

# Search group number tells function how do current search
            if(s[(i*search_group):((i+1)*search_group)] == s[((i+1)*search_group):((i+2)*search_group)]):
                num_squares += 1
            # Due slices being half-inclusive can't use signed (negative) integers in the slices as I won't be able to handle all cases the same
            # To select the last two characters I'll need to do something like [-2:], whilst other characters would be [-3:-1]
            # So instead just repeat the above but start off by +1
            if(isOdd(len(s))):
                if(s[(i*search_group)+1:((i+1)*search_group)+1] == s[((i+1)*search_group)+1:((i+2)*search_group)+1]):
                    num_squares += 1

    return num_squares



# TODO: make the conditionals actually compare the strings




def isOdd(s):
    if(s % 2 == 0):
        return False
    else:
        return True

print(count_squares("1231233"))

#7+6+4 = 17 iterations for 7 characters
# Process:
# select each group of 2 from start and continue till the end
# Then do again but this time starting from the end
# Increase search group to 3 and repeat

# If search group greater than half of total length break as no more squares are possible
# If string length is even then skip search from end as all possible matches for that search group have been found
