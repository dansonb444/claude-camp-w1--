"""根据身高(米)、体重(公斤)计算 BMI 并给出简要健康建议。"""
height = float(input("身高 (米): "))
weight = float(input("体重 (公斤): "))
bmi = weight / (height ** 2)
print(f"\n您的 BMI: {bmi:.2f}")
if bmi < 18.5:
    print("建议: 偏瘦，注意营养与力量训练，必要时咨询营养师。")
elif bmi < 24:
    print("建议: 体重在常见健康范围内，保持均衡饮食与规律运动。")
elif bmi < 28:
    print("建议: 超重趋势，可适当控制热量并增加有氧活动。")
else:
    print("建议: 肥胖相关风险升高，建议逐步减重并咨询医生。")
