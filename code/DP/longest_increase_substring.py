def LIS(arr, n):
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1) # 获取最长上升子序列的长度数组dp

    '''
    接下来解释如何根据求出的dp数组得到最长递增子序列。以题目的例子来说明，arr={2,1,5,3,6,4,8,9,7}，求出的数组dp={1,1,2,2,3,3,4,5,4}。具体求解步骤如下：

    1、遍历dp数组，找到最大值以及位置。在本例中最大值为5，位置为7，说明最终的最长递增子序列的长度为5，并且应该以arr[7]这个数（arr[7]=9）结尾。
    
    2、从arr数组的位置7开始从右向左遍历。如果对某一个位置i，既有arr[i]<arr[7]，又有dp[i]=dp[7]-1，说明arr[i]可以作为最长递增子序列的倒数第二个数。在本例中，arr[6]<arr[7]，并且dp[6]=dp[7]-1，所以8应该作为最长递增子序列的倒数第二个数。
    
    3、从arr数组的位置6开始继续向左遍历，按照同样的过程找到倒数第三个数。在本例中，位置5满足arr[5]<arr[6]，并且dp[5]=dp[6]-1，同时位置4也满足。选arr[5]或者arr[4]作为倒数第三个数都可以。
    
    4、重复这样的过程，直到所有的数都找出来。
    '''
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

print(LIS([1, 5, 3, 2, 6, 7, 4, 8], len([1, 5, 3, 2, 6, 7, 4, 8])))