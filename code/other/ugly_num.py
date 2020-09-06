class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        if n == 1:
            return 1

        list_ugly_num = [1]

        index = 1
        i, j, k = 0, 0, 0
        while index < n:
            # 因为丑数的质因子为2,3,5，那么所有的丑数都是由这三个数构成的，因此可以使用分批上岗的思路，每次选择乘以了2,3,5后最小的数作为最新的数，并使被选中的位置加1
            new_ugly_num = min(list_ugly_num[i] * 2, list_ugly_num[j] * 3, list_ugly_num[k] * 5)

            if list_ugly_num[i] * 2 == new_ugly_num:
                i += 1
            if list_ugly_num[j] * 3 == new_ugly_num:
                j += 1
            if list_ugly_num[k] * 5 == new_ugly_num:
                k += 1

            list_ugly_num.append(new_ugly_num)
            index += 1

        return list_ugly_num[-1]






