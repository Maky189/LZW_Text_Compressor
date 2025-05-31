#The LZW compression algorithm:
    # Begin empty sequence;
    # Read a symbol (x) from the message to encode
    # If is the end of the message then go to the end line
    # Generate a sequence (Sx) from the concatenation of S with x (Sx = S + x)
    # If Sx can be found in the dictionary:
        # S = SX
        # go read the symbol again
    # If Sx can not be found in the dictionary:
        # Omit the encoding of S;
        # Sx is put in the dictionary
        # and S is made with the symbol of x
        # go read the symbol again
    # Omit encode of S

    #ABABABA -> 1235

dictionary = {}
def encode(sequence: str) -> str:
    #Begin empty sequence
    result = ""
    counter = 1

    for char in sequence:
        if char not in dictionary:
            dictionary[char] = counter
            counter += 1


    # Read a symbol (x) from the message to encode
    first = sequence[0]
    for char in sequence[1:]:
        # go read the symbol again
        # Generate a sequence (Sx) from the concatenation of S with x (Sx = S + x)
        Sx = first + char
        # If Sx can be found in the dictionary:
        if Sx in dictionary:
            # S = SX
            first += char
        else:
            # Omit the encoding of S;
            result += str(dictionary[first])
            # Sx is put in the dictionary
            dictionary[Sx] = counter
            counter += 1
            # and S is made with the symbol of x
            first = char



    # If is the end of the message then go to the end line
    return result + str(dictionary[first])


"""
PSEUDOCODE
1    Initialize table with single character strings
2    OLD = first input code
3    output translation of OLD
4    WHILE not end of input stream
5        NEW = next input code
6        IF NEW is not in the string table
7               S = translation of OLD
8               S = S + C
9       ELSE
10              S = translation of NEW
11       output S
12       C = first character of S
13       OLD + C to the string table
14       OLD = NEW
15   END WHILE
"""
def decode(sequence: str) -> str:
    codes = [int(i) for i in sequence]
    #Initialize table with single character strings
    result = ""

    #Inverted the old dictionary
    inverted = {v: k for k, v in dictionary.items()}

    #Go thrught all the code and conevert them back to text
    for each in codes:
        result += inverted[each]

    return result
