


def bni():
    weight = float(input('체중 입력:'))
    height = float(input('키 입력:'))
    bmi = weight / ((height /100) ** 2)
    bmi = int(bmi)


    if bmi <= 18.5:
        print(f'당신의 bmi는 {bmi} 이고 저체중 입니다.')
    elif bmi < 22.9:
        print(f'당신의 bmi는 {bmi} 이고  정상체중 입니다.')
    elif bmi < 24.9:
        print(f'당신의 bmi는 {bmi} 이고  과체중 입니다.')
    else:
        print(f'당신의 bmi는 {bmi} 이고  비만 입니다.')
    