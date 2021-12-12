import functions
f = input("주민등록번호 앞 6자리를 입력해주세요!\n")
a = input("주민등록번호 뒤 7자리를 입력해주세요!\n")
code = f + "-" + a
args = code.split("-")
print("생년월일 "+"="*50)
if (int(args[1][0]) <= 2):
    print("년도: "+"19"+args[0][0:2])
else:
    print("년도: "+"20"+args[0][0:2])
print("월: "+args[0][2:4])
print("일: "+args[0][4:])
print("주민등록번호 뒷자리 분석"+"="*35)
after = functions.after(code)
print("성별: "+after['sex'])
print("도시: "+after['city'])
print("읍/면/동: "+str(after['local']))
print("접수 순서: "+str(after['order']))
print("확인 번호: "+str(after['check']))