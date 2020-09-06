import sys

while True:
    try:
        line = sys.stdin.readline().strip()
        if not line:
            break
        hex_num = line[2:]
        hex_list = '0123456789ABCDEF' # 16进制的所有值

        i = 0
        res = 0
        l = len(hex_num)
        while i < l:
            res += hex_list.index(hex_num[i]) * (16 ** (l - i - 1))
            i += 1
        print(res)
    except:
        pass