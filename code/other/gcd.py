def gcd(x, y):
    # 两数求最大公约数
    temp = x % y
    while temp != 0:
        x = y
        y = temp
        temp = x % y
    return y