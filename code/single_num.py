class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] = True
            else:
                num_dict.setdefault(num, False)

        for key in num_dict:
            if not num_dict[key]:
                return key
