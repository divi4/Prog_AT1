def count_squares(s):
    num_squares = 0

    for search_group in range(1, (len(s)//2)+1): # Will end loop after reaching half of the length of the string, as no more matches are possible beyond this
        print("Start of outer loop search group:", search_group)
        for i in range(((len(s))//search_group) + 1):
            # print("---------Inner loop-------:", i)
 # The number of iterations a search needs to go through and check an entire string will never exceed the length of the string

# Search group number tells function how do current search
            if((((i+2)*search_group)) > len(s)):
                break
            elif(int(s[(i*search_group):((i+1)*search_group)]) == int(s[((i+1)*search_group):((i+2)*search_group)])):
                print("**Found in even**:", s[(i*search_group):((i+1)*search_group)])
                num_squares += 1


# Can compare however we end up exceed the available range:
# [0,2][2,4][4,6][4:8]  - The loop continues beyond half-way point

            # Due slices being half-inclusive can't use signed (negative) integers in the slices as I won't be able to handle all cases the same
            # To select the last two characters I'll need to do something like [-2:], whilst other characters would be [-3:-1]
            # So instead just repeat the above but start off by +1

            # May need to use negative slices as having problems with the index number going beyond the available range
            # if(((i+2)*search_group) > (len(s)/2)):
            #     break

            # if((((i+2)*search_group)) > len(s)):
            #         print("Even second exceeds search, break")
            # print("First even:", (i*search_group), ((i+1)*search_group))
            # print("Second even:", ((i+1)*search_group), ((i+2)*search_group))
            # print("\n")
            # if(search_group != 1):
            #     if((((i+2)*search_group)+1) > len(s)):
            #             print("Odd second exceeds search, break")
            #     print("First odd:", ((i*search_group)+1), (((i+1)*search_group)+1))
            #     print("Second odd:", (((i+1)*search_group)+1), (((i+2)*search_group)+1))
# Does search offsetted by one
# TODO do the offsetting search_group - 1 times to find all

            if(search_group != 1):  # To avoid doubling up
                for j in range(1, search_group):  # 0 = no offset, search_group-1 is the maximum possible offset before repeat
                    # print("j", j)
                    # print("i", i)
                    if((((i+2)*search_group)+j) > len(s)):  # TODO check if still need this
                        # print("oi")
                        break
                    # the addition to i represents the i value in the next iteration or one after that
                    # slices are like: is 1st iteration:2nd == 2nd:3rd?
                    elif(int(s[(i*search_group)+j:((i+1)*search_group)+j]) == int(s[((i+1)*search_group)+j:((i+2)*search_group)+j])):
                        print("**Found in odd**:", s[((i)*search_group)+j:((i+1)*search_group)+j])
                        num_squares += 1

    return num_squares


# TODO: 
# Missing 23 on first iteration
# Getting 12 on 1st instead of 2nd,33 on 2nd instead of 3rd


print("Number of squares: {}".format(count_squares("123123123123")))


#7+6+4 = 17 iterations for 7 characters
# Process:
# select each group of 2 from start and continue till the end
# Then do again but this time starting from the end
# Increase search group to 3 and repeat

# If search group greater than half of total length break as no more squares are possible
# If string length is even then skip search from end as all possible matches for that search group have been found

# len(s)//search_group would give the number of possible iterations for a search_group without going out of bounds
# can update this number when do offset: len(s) - offset//search_group to avoid out of bounds