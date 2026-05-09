"""根据餐费与小费比例计算应付总额。"""
bill = float(input("餐费金额 (元): "))
rate = float(input("小费比例 (%，例如 15 表示 15%): "))
tip = bill * rate / 100.0
total = bill + tip
print()
print(f"小费: {tip:.2f} 元")
print(f"总金额 (餐费 + 小费): {total:.2f} 元")
