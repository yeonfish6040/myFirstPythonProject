import re
import time
import functions

regex = "^[a-zA-Z]*$"
regex = re.compile(regex, flags=re.I)
pw = input("please type english only password\n")
pw = pw.lower()
ok = True
pwMatched = True
while ok:
    if regex.match(pw):
        ok = False
        continue
    string = input("please retype the password. cause incorrect type\n")
leng = len(pw)
charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = "a"*leng
start_time = time.time()
while pwMatched:
    if result == pw:
        pwMatched = False
        break
    increased = functions.str_increaser(result, charList, 1)
    if increased != "str_increaser(): Input already max in charset":
        result = increased
    else:
        ValueError(increased)
print("finished!"+" - "+result)
print("--- %s seconds --- " % round(time.time() - start_time, 2))

# while ok :
#    print("hello")