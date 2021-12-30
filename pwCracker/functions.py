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