import sys

'''
获取最长子串长度
'''
if __name__ == '__main__':
    while True:
        try:
            s1 = sys.stdin.readline().strip()
            if not s1:
                break
            s2 = sys.stdin.readline().strip()

            i, j = 0, 0
            n1, n2 = len(s1), len(s2)

            dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
            index = 0 # 子串的起始位置
            max_num = 0 # 最长子串的长度

            for i in range(1, n1):
                for j in range(1, n2):
                    if s1[i - 1] == s2[j - 1]: # 相同则累加，反之则不做处理
                        dp[i][j] = dp[i - 1][j - 1] + 1

                        if dp[i][j] > max_num: # 获取最长子串长度
                            max_num = dp[i][j]
                            index = i + 1 # 记录最长子串的终止位置
            print(s1[index - max_num: index], max_num)
        except:
            pass