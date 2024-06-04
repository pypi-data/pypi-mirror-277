def bmi_find():
    height = float(input("내 키를 입력 : "))
    weight = float(input("내 체중을 입력 : "))
    bmi = weight /((height/100) * (height/100))
    print("키는 {}, 체중은 {}".format(height,weight))

    if bmi <= 18.5:
        print("나의 BMI 지수는 {:.2f}이고, 저체중입니다.".format(bmi))
    elif bmi <= 22.9:
        print("나의 BMI 지수는 {:.2f}이고, 정상입니다.".format(bmi))
    elif bmi <= 24.9:
        print("나의 BMI 지수는 {:.2f}이고, 과체중입니다.".format(bmi))
    else:
        print("나의 BMI 지수는 {:.2f}이고, 비만입니다.".format(bmi))             