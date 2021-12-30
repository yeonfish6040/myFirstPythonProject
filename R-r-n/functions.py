def getCity(num):
    a = list(range(0, 9))
    b = list(range(9, 13))
    c = list(range(13, 16))
    d = list(range(16, 26))
    e = list(range(26, 35))
    f = list(range(35, 40))
    g = [40]
    h = list(range(41, 48))
    i = list(range(48, 55))
    j = list(range(57, 67))
    k = list(range(55, 57))
    l = [67, 68, 76]
    n = [70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81]
    m = [82, 83, 84, 86, 87, 88, 89, 90, 91, 92]
    o = [85]
    p = list(range(93, 96))
    q = [44, 49]
    cities = {"Seoul": a, "Busan": b, "Incheon": c, "Gyeonggi-do": d, "Gangwon-do": e, "Chungcheongbuk-do": f, "Daejeon": g, "Chungcheongnam-do": h, "Jeollabuk-do": i, "Jeollanam-do": j, "Gwangju": k, "Dae-gu": l, "Gyeongsangbuk-do": n, "Gyeongsangnam-do": m, "Ulsan Metropolitan City": o, "Jeju Special City": p, "Sejong": q}
    num = int(num)
    for key, value in cities.items():
        if num in value:
            return key

def after(code):
    args = code.split("-")
    main = args[1]
    if (int(args[1][0]) >= 3):
        if int(args[0][0:2]) >= 20:
            return "알수없음"
    if (int(main[0]) % 2 == 1):
        sex = "남성"
    else:
        sex = "여성"
    city = main[1:3]
    city = getCity(city.lstrip("0"))
    local = main[3:5]
    order = main[5]
    check = main[6]
    result = {"sex": sex, "city": city, "local": int(local), "order": int(order), "check": int(check)}
    return result