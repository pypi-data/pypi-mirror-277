# BMI = weight / (height2 * height2) # 18.5 이하 저체중 23-24.9 과체중 / 25 이상 비만 
height = int(input("신장을 입력하세요.(cm) :"))
weight = int(input("체중을 입력하세요.(kg) : "))
height2 = height/100
BMI = round(weight / (height2 * height2), 2) # 18.5 이하 저체중 23-24.9 과체중 / 25 이상 비만 
if BMI >= 25:
    print(f'당신의 신장은 {height}cm이고 체중은 {weight}kg이며, BMI지수는 {BMI}입니다. 이는 비만으로 감량을 권장드립니다.')
elif 24.9 >= BMI >= 23:
    print(f'당신의 신장은 {height}cm이고 체중은 {weight}kg이며, BMI지수는 {BMI}입니다. 이는 과체중으로 약간의 감량이 필요합니다.')
elif 22.9 >= BMI > 18.5:
     print(f'당신의 신장은 {height}cm이고 체중은 {weight}kg이며, BMI지수는 {BMI}입니다. 이는 정상으로 매우 건강합니다.')
elif BMI <= 18.5:
    print(f'당신의 신장은 {height}cm이고 체중은 {weight}kg이며, BMI지수는 {BMI}입니다. 이는 저체중으로 증량이 필요합니다.')