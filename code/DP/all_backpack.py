import sys

def cal_revenue(arr, budget):
    res = []
    for item in arr:
        current_revenue = int(item[1]) * (1 + float(item[2][:-1]) * 0.01)
        num = 0
        while num * int(item[1]) <= budget:
            num += 1
        current_res = [item[0], num - 1, int(item[1]), current_revenue]
        res.append(current_res)

    return res


'''
输入：
total,78
新网1号,5,2.0%
新网2号,12,2.5%
新网3号,16,2.8%
新网4号,17,2.9%
null
输出：
新网2号,12
新网3号,32
新网4号,34
'''
if __name__ == '__main__':
    items = []
    budget = 0
    try:
        while True:
            line = sys.stdin.readline().strip()
            if line == 'null':
                break
            items.append(line.split(','))
        budget = int(items[0][1])
        items = items[1:]
    except:
        pass
    items = cal_revenue(items, budget)
    n = len(items)

    '''
    完全背包
    '''
    w = [0] * (n + 1) # 每件体积
    v = [0] * (n + 1) # 价值

    for i in range(1, n + 1):
        v[i], w[i] = items[i - 1][3], items[i - 1][2]

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            if j < w[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - w[i]] + v[i])

    '''
    打印完全背包的选择方案
    '''
    index = budget
    choose = []
    for i in range(n, 0, -1):
        while (index - w[i]) >= 0:
            if ((dp[i][index - w[i]] + v[i]) > dp[i - 1][index]):
                index -= w[i]
                choose.append(i)
            else:
                break

    final_dict = {}
    for item in choose:
        if item - 1 not in final_dict:
            final_dict.setdefault(item - 1, 1)
        else:
            final_dict[item - 1] += 1

    dict_key = sorted(list(final_dict.keys()))

    for key in dict_key:
        print(items[key][0] + ',' + str(items[key][2] * final_dict[key]))

