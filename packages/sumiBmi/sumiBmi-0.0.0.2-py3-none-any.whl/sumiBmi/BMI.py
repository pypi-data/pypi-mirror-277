h = int(input('키를 입력하세요(cm): '))
w = int(input('몸무게를 입력하세요(kg): '))

BMI = round(w/(h/100)**2,2)

if float(BMI) >= 25.0:
    print(f'BMI는 {BMI}, 비만입니다')
elif float(BMI) >= 23.0:
    print(f'BMI는 {BMI}, 과체중입니다')
elif float(BMI) >= 18.5:
    print(f'BMI는 {BMI}, 정상입니다')
elif float(BMI) >= 0:
    print(f'BMI는 {BMI}, 저체중입니다')
else:
    None