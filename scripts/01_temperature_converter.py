"""摄氏度与华氏度互换。"""
print("1) 摄氏 → 华氏   2) 华氏 → 摄氏")
choice = input("请选择 (1/2): ").strip()
if choice == "1":
    c = float(input("请输入摄氏度: "))
    f = c * 9 / 5 + 32
    print(f"{c:.2f} °C = {f:.2f} °F")
elif choice == "2":
    f = float(input("请输入华氏度: "))
    c = (f - 32) * 5 / 9
    print(f"{f:.2f} °F = {c:.2f} °C")
else:
    print("无效选项，请输入 1 或 2。")
