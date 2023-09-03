def count_squares(s):
    num_squares = 0
    decrement = 0

    for search_group in range(2, (len(s)//2)+1): 
        decrement += 1
        for i in range((len(s)//2)-decrement):
            print("Loop:", i)
            if((((i+2)*search_group)) > len(s)):
                    print("Even second exceeds search, break")
            print("First even:", (i*search_group), ((i+1)*search_group))
            print("Second even:", ((i+1)*search_group), ((i+2)*search_group))
            print("\n")
            if((((i+2)*search_group)+1) > len(s)):
                    print("Odd second exceeds search, break")
            print("First odd:", ((i*search_group)+1), (((i+1)*search_group)+1))
            print("Second odd:", (((i+1)*search_group)+1), (((i+2)*search_group)+1))
            print("\n")

    return num_squares


def isIndexValid(index, s):
    if(index > len(s)):
        return -1
    else:
        return index


count_squares("123123354")
# Length 9

# print("123123354"[5:7])

# Can combine the for loops by doing the offset in it
# Start off with 0 offset then increase by one till done full search for that search group
# size 2: 1 offset
# size 3: 2 offsets
# offset times for a size group: (size_group - 1)


# if index > len(s): break
# Always occurs on second slice on the latter of half of it



            # print("Loop:", i)
            # if((((i+2)*search_group)) > len(s)):
            #         print("Even second exceeds search, break")
            # print("First even: ", s[(i*search_group):((i+1)*search_group)])
            # print("Second even:", s[((i+1)*search_group):((i+2)*search_group)])
            # print("\n")
            # if((((i+2)*search_group)+1) > len(s)):
            #         print("Odd second exceeds search, break")
            # print("First odd: ", s[((i*search_group)+1):(((i+1)*search_group)+1)])
            # print("Second odd:", s[(((i+1)*search_group)+1):(((i+2)*search_group)+1)])
            # print("\n")