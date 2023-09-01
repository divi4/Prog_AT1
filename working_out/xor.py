# To do what I want I'll need to select each character
# then do a XOR on it with 1 to get the inverse


# p = "012"
# q = 1

# if((p and not q) or (not p and q)):
#     print("1\n")
# else:
#     print("0 \n")


# if((int(p[0:1]) and not q) or (not int(p[0:1]) and q)):
#     print("1\n")
# else:
#     print("0 \n")


def xor(t):
    q = 1
    inverse = ""
    for count in range(len(t)):
        if((int(t[count:count+1]) and not q) or (not int(t[count:count+1]) and q)):
            inverse += "1"
        else:
            inverse += "0"
    return inverse
    
print(xor("010101101"))



# print((p and not q))
# 1 0 T
# 1 1 F
# 0 0 0
# 0 1 0


# print((p and not q) and (not p and q))
# --> returns False if 1,1 else returns 0
# So if ask == False, then it'll return True when 1,1 
# otherwise it should return False when 1,0

# print((p and not q) and (not p and q) == False)
# --> returns True if 1,0 and False if 1,1






# Create truth table?
# 0 1 T
# 1 1 F
# 0 0 F
# 1 0 T


# if(p == "1" and q == "0"):
#     print("Yay \n")
# elif(p == "0" and q == "1"):
#     print("Yay \n")
# else:
#     print("Nope \n")

