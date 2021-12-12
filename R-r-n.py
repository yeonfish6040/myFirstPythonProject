code = '123456-12345678';
args = code.split("-");
if int(args[1][0]) <= 2:
    print("생년월일 "+"="*50)
    print("년도: "+"19"+args[0][0:2])
    print("월: "+args[0][2:4])
    print("일: "+args[0][4:])
    if int(args[1][0]) == 1:
        print("남성")
    else:
        print("여성")
    print("주민등록번호 뒷자리: "+args[1])
else:
    print("생년월일 "+"="*50)
    print("년도: "+"20"+args[0][0:2])
    print("월: "+args[0][2:4])
    print("일: "+args[0][4:])
    if int(args[1][0]) == 3:
        print("남성")
    else:
        print("여성")
    print("주민등록번호 뒷자리: "+args[1])