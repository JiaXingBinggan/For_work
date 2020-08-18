import math
import sys
def judge_prime_number(num):
    i = 2
    flag = True
    while flag and i <= math.sqrt(num):
        if num % i == 0:
            flag = False
        i += 1
    return flag

def group_even_odd(number_list): # 划分偶数和奇数，因为大于2的质（素）数都可以由奇数和偶数组成；因此就转换为了二分图最大匹配的问题
    even, odd = [], []
    for num in number_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

def build_matrix(odd, even): # 建立映射关系，某个坐标值为1，则代表能够odd[i]和even[j]能够之和是素数
    matrix = [[0] * len(even) for _ in range(len(odd))]

    for i, o_n in enumerate(odd):
        for j, e_n in enumerate(even):
            if judge_prime_number(e_n + o_n):
                matrix[i][j] = 1
    return matrix

def find(x): # 匈牙利算法
    '''
    输入的是奇数，希望能找到最大的匹配
    :param x:
    :return:
    '''
    for index, e_n in enumerate(even): # 对于每个奇数都要去遍历所有偶数
        if matrix[x][index] == 1 and used[index] == 0: # 如果能够组成素数，并且没有被标记过则把当前的偶数位置标记出来
            used[index] = 1
            if connect[index] == -1 or find(connect[index]): # 如果当前偶数没有和任何奇数配对 或者 当前偶数可以和其它奇数配对
                connect[index] = x # 把当前偶数和输入的奇数配对
                return True
    return False

while True:
    try:
        count = sys.stdin.readline().strip()
        if not count:
            break
        count = int(count)
        if count % 2 != 0:
            print(0)
            break
        number_list = map(int, sys.stdin.readline().strip().split())
        even, odd = group_even_odd(number_list)

        matrix = build_matrix(odd, even)
        connect = [-1 for _ in range(len(even))] # 偶数的连接
        count_1 = 0
        for i in range(len(odd)):
            used = [0 for _ in range(len(even))] # 每次遍历都需要置零
            if find(i):
                count_1 += 1
        print(count_1)
    except:
        pass

