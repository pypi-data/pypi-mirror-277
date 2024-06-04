def BMI(height, weight):
    bmi = weight / ((height/100)**2)
    a = ''
    if bmi >= 25.0:
        a = '비만'
    
    elif bmi >= 23.0:
        a = ('과체중')

    elif bmi >= 18.5:
        a = ('정상')
    
    elif bmi < 18.5:
        a = ('저체중')
    
    print(f'My BMI: {bmi:0.1f} // 나의 BMI(신체질량지수)는 {bmi:0.1f}이고 {a}입니다')


