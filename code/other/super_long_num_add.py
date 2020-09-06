import sys


def move(num1, num2):
    move = 0
    sum_ = num1 + num2
    if sum_ >= 10:
        move = 1
    new_num = sum_ % 10

    return move, new_num

'''
请设计一个算法完成两个超长正整数的加法。 

示例1
输入
99999999999999999999999999999999999999999999999999
1

输出
100000000000000000000000000000000000000000000000000

'''
if __name__ == '__main__':
    while True:
        try:
            line1 = sys.stdin.readline().strip()
            if not line1:
                break
            line2 = sys.stdin.readline().strip()

            line1, line2 = list(line1), list(line2)
            n1, n2 = len(line1), len(line2)
            if n1 > n2:
                line2 = ['0'] * (n1 - n2) + line2
            else:
                line1 = ['0'] * (n2 - n1) + line1

            n = len(line1)
            new_string = ''
            move_flag = 0
            for i in range(n - 1, -1, -1):
                move_, new_num = move(int(line1[i]), int(line2[i]))
                move_flag = move_
                if move_:
                    line1[i - 1] = str(int(line1[i - 1]) + 1)
                new_string += str(new_num)
            if move_flag:
                new_string += '1'
            print(''.join(list(reversed(new_string))))
        except:
            pass
