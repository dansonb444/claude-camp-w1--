"""按指定长度生成随机字母数字密码。"""
import random
import string

length = int(input("密码长度: "))
if length < 1:
    print("长度至少为 1。")
else:
    chars = string.ascii_letters + string.digits
    pwd = "".join(random.choice(chars) for _ in range(length))
    print("生成的密码:", pwd)
