import sys

if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    line2 = sys.stdin.readline().strip()

    n, m = tuple(map(int, line1.split(' ')))
    A_nums = list(map(int, line2.split(' '))) # A的带宽
    if len(A_nums) != n: # 不合法输入
        print(0)

    customer_budget = {} # 字典包括带宽和预算
    for _ in range(m):
        line = sys.stdin.readline().strip()
        if not line:
            break
        else:
            current_num_budget = tuple(map(int, line.split(' ')))
            if current_num_budget[0] not in customer_budget:
                customer_budget.setdefault(current_num_budget[0], [current_num_budget[1]])
            else:
                customer_budget[current_num_budget[0]].append(current_num_budget[1])
    sells = 0
    for a_num in A_nums:
        max_value = 0
        max_index = 0
        while a_num > 0:
            if a_num in customer_budget and customer_budget[a_num] and max(customer_budget[a_num]) > max_value:
                max_value = max(customer_budget[a_num])
                max_index = a_num
            a_num -= 1
        customer_budget[max_index].remove(max_value)
        sells += max_value
    print(sells)