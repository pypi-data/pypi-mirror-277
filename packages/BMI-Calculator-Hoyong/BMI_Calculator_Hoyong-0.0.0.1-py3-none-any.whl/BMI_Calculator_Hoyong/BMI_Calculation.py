def BMI_Calculation(height : float, weight : float) -> None:
    BMI = weight/height**2
    BMI = round(BMI,1)
    if BMI <= 18.5:
        print(f'BMI 지수는 {BMI}입니다. 당신은 저체중입니다.')
    elif 18.5 < BMI <= 22.9:
        print(f'BMI 지수는 {BMI}입니다. 당신은 정상입니다.')
    elif 23.0 < BMI <= 24.9:
        print(f'BMI 지수는 {BMI}입니다. 당신은 과체중입니다.')
    else:
        print(f'BMI 지수는 {BMI}입니다. 당신은 비만입니다.')
         
BMI_Calculation(1.7,60)
