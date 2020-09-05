class Solution(object):
    def isStraight(self, nums):
        """
        从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

        示例 1:
        输入: [1,2,3,4,5]
        输出: True

        示例 2:
        输入: [0,0,1,2,5]
        输出: True
        :type nums: List[int]
        :rtype: bool
        """
        # 最主要的公式就是，因为限定了5个连续的顺子，所以如果满足max(nums)-min(nums)肯定是小于5的
        no_zero_nums = [num for num in nums if num] # 首先选择出非零0的数，用于判断是否有重复的
        # 如果集合中的数字长度小于原始非零数字的数组长度，则一定存在重复的，则提前返回不是顺子False
        return len(set(no_zero_nums)) == len(no_zero_nums) and max(no_zero_nums) - min(no_zero_nums) < 5
