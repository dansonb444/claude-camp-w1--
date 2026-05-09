"""根据餐费 (AUD) 与小费比例计算小费与总金额。"""
bill = float(input("餐费金额 (AUD): "))
rate = float(input("小费比例 (%，例如 15 表示 15%): "))
tip = bill * rate / 100.0
total = bill + tip
print()
print("------------------------")
print(f"餐费         : ${bill:.2f}")
print(f"小费 ({rate}%) : ${tip:.2f}")
print(f"总金额       : ${total:.2f}")
