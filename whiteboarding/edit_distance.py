#!/usr/bin/python3
"""
Return True if the string requires less than one edit
Return False if the string requires more than one edit
"""
def editDistance(string1, string2):
    """
    Return: True if the string requires less than one edit, False otherwise
    """
    if len(string1) >=len(string2):
        longerStr = string1
        shorterStr = string2
    else:
        longerStr = string2
        shorterStr = string1
    # check if the length between the two strings is greater then two
    if len(longerStr) - len(shorterStr) > 1:
        return False
    diffCounter = 0
    i = j = 0
    if len(longerStr) - len(shorterStr) == 1:
        while i <  len(shorterStr):
            # find the shorter length and loop through that range
            if shorterStr[i] == longerStr[j]:
                # find the shorter length and loop through that range
                i += 1
                j += 1
            else:
                j += 1
                diffCounter += 1
    else:
        for i in range(len(shorterStr)):
            if shorterStr[i] != longerStr[i]:
                diffCounter += 1
    if diffCounter > 1:
        return False
    return True


print("string1:{:s} string2:{:s}, editDistance:{}".format("hello", "hell", editDistance("hello", "hell")))
print("string1:{:s} string2:{:s}, editDistance:{}".format("hello", "hel", editDistance("hello", "hel")))
print("string1:{:s} string2:{:s}, editDistance:{}".format("hello", "heeeo", editDistance("hello", "heeeo")))
print("string1:{:s} string2:{:s}, editDistance:{}".format("hello", "hllo", editDistance("hello", "hllo")))
print("string1:{:s} string2:{:s}, editDistance:{}".format("hello", "hallo", editDistance("hello", "hallo")))
