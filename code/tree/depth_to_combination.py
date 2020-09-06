import sys

'''
计算组合数c(n,m)
c(n, m​)=c(n - 1, m - 1)+c(n - 1, m)
'''
def compute_c_m_n(n, m):
    if m == n:
        return 1
    elif m == 1:
        return n
    else:
        return compute_c_m_n(n - 1, m - 1) + compute_c_m_n(n - 1, m)

'''
给定节点数量，以及各节点的深度
求，能够构成这种情况的二叉树有多少。
'''
if __name__ == '__main__':
    while True:
        try:
            line1 = sys.stdin.readline().strip()
            if not line1:
                break
            line2 = sys.stdin.readline().strip()

            node_num = int(line1)
            depths = list(map(int, line2.split(' ')))
            if node_num != len(depths):
                print(0)
                break
            depths.sort()
            depth_count_dict = {} # key=depth,value=count

            for depth in depths:
                if depth not in depth_count_dict:
                    depth_count_dict.setdefault(depth, 1)
                else:
                    depth_count_dict[depth] += 1

            depth_counts = list(depth_count_dict.items())
            count = 1
            for i, depth_count in enumerate(depth_counts):
                if i == 0 and depth_count[0] != 0: # 最小深度不为0时，不合法
                    print(0)
                    break
                if i > 0:
                    if depth_count[1] > 2 ** depth_count[0] or depth_count[0] != depth_counts[i - 1][0] + 1: # 当第n层的节点数不是n-1节点数加一时，或者，0134，缺少深度为2的节点
                        print(0)
                        break
                    n = depth_counts[i - 1][1] * 2
                    m = depth_count[1]
                    count *= (int(compute_c_m_n(n, m)) % (10 ** 9 + 7))
            print(count)
        except:
            pass