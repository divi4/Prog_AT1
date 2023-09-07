def main():
    s = input("Input numbers 1-3 in a sequence to see number of squares present: ")
    print("Number of squares in {}: {} squares".format(s, count_squares(s)))


def count_squares(s):
    num_squares = 0

    for search_group in range(1, (len(s)//2) + 1):  # Search group number tells function the character size of each group it'll compare in the iteration
        for i in range((len(s)//search_group) - 1):  # Range gives the maximum number of possible squares in a given search group for a current offset based on the length of the string
            for offset in range(search_group):   # 0 = no offset, final value of search_group is the maximum possible offset in the current search
                if((((i + 2)*search_group) + offset) > len(s)):  # Checks if the sum will be larger than the length of s
                    break
                elif(int(s[(i*search_group) + offset:((i + 1)*search_group) + offset]) == int(s[((i + 1)*search_group) + offset:((i + 2)*search_group) + offset])):
                    num_squares += 1

    return num_squares


main()