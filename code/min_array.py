class Solution(object):
    def minArray(self, numbers):
        """
        把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
        https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
        :type numbers: List[int]
        :rtype: int
        """
        if not numbers:
            return

        first, last = 0, len(numbers) - 1

        while first < last:
            mid = (first + last) // 2  # 二分法节省寻找成本
            if numbers[mid] < numbers[last]:  # 当中值比最右边的值小，说明从mid-last区间的都是升序，则往左靠
                last = mid
            elif numbers[mid] == numbers[last]:  # 当相等时，往左靠
                last -= 1
            else:  # 当中值比最右边的值大时，说明first-mid区间的是降序，则往右靠
                first = mid + 1

        return numbers[first]