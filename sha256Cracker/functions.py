def str_increaser(mystr, charset, n_increase):

    def replace_chr_in_str(mystr, index, char):
        mystr = list(mystr)
        mystr[index] = char
        return ''.join(mystr)

    def local_increase(mystr, charset):
        l_cs = len(charset)
        if (charset.index(mystr[-1]) < l_cs - 1):
            mystr = replace_chr_in_str(mystr, -1, charset[charset.index(mystr[-1]) + 1])
        else:
            mystr = replace_chr_in_str(mystr, -1, charset[0])
            mystr = local_increase(mystr[:-1], charset) + mystr[-1]
        return mystr

    if (mystr == charset[-1] * len(mystr)):
        return "str_increaser(): Input already max in charset"
    else:
        for i in range(n_increase):
            mystr = local_increase(mystr, charset)

    return mystr

def charList():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '[', '}', ']', '|', '\\', ':', ';', '"', '\'', ',', '<', '.', '>', '/', '?', ' ']

def getHash(string):
    import hashlib
    return hashlib.sha256(string.encode()).hexdigest()