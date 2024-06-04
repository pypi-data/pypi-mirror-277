h = int(input('키를 입력하세요(cm): '))
w = int(input('몸무게를 입력하세요(kg): '))

BMI = round(w/(h/100)**2,2)

def BMI_test():
    if BMI >= 25.00:
        print(f'BMI는 {BMI}, 비만입니다')
    elif BMI >= 23.00:
        print(f'BMI는 {BMI}, 과체중입니다')
    elif BMI >= 18.50:
        print(f'BMI는 {BMI}, 정상입니다')
    elif BMI >= 0:
        print(f'BMI는 {BMI}, 저체중입니다')