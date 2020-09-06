import sys

def reverse(arr):
    i, j = 0, len(arr) - 1

    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr

def LIS(arr, n):
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_dp = max(dp)
    max_dp_index = 0
    for i in range(n - 1, -1, -1):
        if dp[i] == max_dp:
            max_dp_index = i
            break

    res = [arr[max_dp_index]]
    while max_dp_index > 0:
        temp_index = 0
        for i in range(max_dp_index - 1, -1, -1):
            if arr[max_dp_index] > arr[i] and dp[i] == dp[max_dp_index] - 1:
                res.insert(0, arr[i])
                temp_index = i
                break
        max_dp_index = temp_index

    return res

if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    n = int(line)
    arr = list(map(int, sys.stdin.readline().strip().split(' ')))

    if n != len(arr):
        print(0)
        sys.exit(0)

    r = reverse(arr)

    lis_arr = LIS(r, n)

    if len(lis_arr) == n:
        print(1)
    else:
        count = 0
        while len(lis_arr) > 1:
            max_item = max(lis_arr)
            for item in lis_arr:
                if item != max_item:
                    arr.remove(item)
            count += 1
            lis_arr = LIS(arr, len(arr))

        print(count)
