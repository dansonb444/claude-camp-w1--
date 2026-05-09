"""根据身高(厘米)、体重(公斤)计算 BMI 并给出简要健康建议。"""
height_cm = float(input("身高 (厘米): "))
weight_kg = float(input("体重 (公斤): "))
h_m = height_cm / 100.0
bmi = weight_kg / (h_m * h_m)
print(f"\n您的 BMI: {bmi:.1f}")
if bmi < 18.5:
    print("建议: 偏瘦，注意营养与力量训练，必要时咨询营养师。")
elif bmi < 24:
    print("建议: 体重在常见健康范围内，保持均衡饮食与规律运动。")
elif bmi < 28:
    print("建议: 超重趋势，可适当控制热量并增加有氧活动。")
else:
    print("建议: 肥胖相关风险升高，建议逐步减重并咨询医生。")
