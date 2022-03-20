import math

def allChars():
    allChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', '\'', '<', ',', '>', '.', '?', '/', '`', '』', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    return allChars
def allChars2num():
    allChars2num = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26', 'A': '27', 'B': '28', 'C': '29', 'D': '30', 'E': '31', 'F': '32', 'G': '33', 'H': '34', 'I': '35', 'J': '36', 'K': '37', 'L': '38', 'M': '39', 'N': '40', 'O': '41', 'P': '42', 'Q': '43', 'R': '44', 'S': '45', 'T': '46', 'U': '47', 'V': '48', 'W': '49', 'X': '50', 'Y': '51', 'Z': '52', '0': '53', '1': '54', '2': '55', '3': '56', '4': '57', '5': '58', '6': '59', '7': '60', '8': '61', '9': '62', '~': '63', '!': '64', '@': '65', '#': '66', '$': '67', '%': '68', '^': '69', '&': '70', '*': '71', '(': '72', ')': '73', '_': '74', '-': '75', '+': '76', '=': '77', '{': '78', '}': '79', '[': '80', ']': '81', '|': '82', '\\': '83', ':': '84', ';': '85', '"': '86', '\'': '87', '<': '88', ',': '89', '>': '90', '.': '91', '?': '92', '/': '93', '`': '94', '』': '95', '1': '96', '2': '97', '3': '98', '4': '99', '5': '100', '6': '101', '7': '102', '8': '103', '9': '104', '0': '105'}
    return allChars2num
chars = allChars()
chars2num = allChars2num()
print(len(chars))
print(len(chars2num))
def encode(string, key):
    # get all chars
    chars = allChars()
    # get num from chars
    chars2num = allChars2num()
    # change string to using variable
    inputString = string
    # change key to using variable
    decode = key
    # declare temp
    temp = ""
    # loop through decode
    for i in range(len(decode)):
        # change decode chars to num and save in temp
        temp = temp + str(chars2num[decode[i]])
    # change temp to int
    temp = int(temp)
    # declare text
    text = ""
    # loop through inputString
    for i in range(len(inputString)):
        # get num from inputString and multiply by temp
        num = int(chars2num[inputString[i]])*temp
        # get index from num
        index = num % len(chars)
        text = text + chars[index]
    lenth = len(text)
    ntext = ""  
    loopnum = 0
    if math.floor(lenth/40) != 0:
        loopgo = int(math.floor(lenth/40))
        loopOk = False
        loopcount = 0
        while not loopOk:
            ntext = ntext + "\n" + text[loopnum:loopnum + 40]
            loopnum = loopnum + 40
            loopcount += 1
            if loopcount == loopgo:
                ntext = ntext + "\n" + text[loopnum:lenth]
                loopOk = True
    else:
        ntext = text
    return ntext
def decode(string, key):
    chars = allChars()
    chars2num = allChars2num()
    temp = ""
    for i in range(len(key)):
        temp = temp + str(chars2num[key[i]])
    temp = int(temp)
    text = ""
    for i in list(string):
        for i2 in chars:
            if encode(i2, key) == i:
                text = text + i2
                break
    return text