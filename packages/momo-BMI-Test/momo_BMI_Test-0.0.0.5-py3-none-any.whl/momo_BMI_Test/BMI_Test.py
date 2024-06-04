def bmi():
    height = int(input("신장을 입력해주세요(소수점 제외).: "))
    weight = int(input("몸무게를 입력해주세요(소수점 제외).: "))
    height_m = height * 0.01
    height_double = height_m * height_m
    bmi_c = weight / height_double
    round_bmi = round(bmi_c, 1)
    if round_bmi <= 18.5 :
        print(f"MY BMI: {round_bmi}".center(40))
        print(f"나의 BMI(신체질량지수)는{bmi} 이고, 저체중입니다.")
    elif round_bmi >= 18.5 and round_bmi <= 22.9 :
        print(f"MY BMI: {round_bmi}".center(40))
        print(f"나의 BMI(신체질량지수)는{round_bmi} 이고, 정상입니다.")
    elif round_bmi >= 23.0 and round_bmi <= 24.9:
        print(f"MY BMI: {round_bmi}".center(40))
        print(f"나의 BMI(신체질량지수)는{round_bmi} 이고, 과체중입니다.")
    elif round_bmi >= 25.0 :
        print(f"MY BMI: {round_bmi}".center(40))
        print(f"나의 BMI(신체질량지수)는{round_bmi} 이고, 비만입니다.")


