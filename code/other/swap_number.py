class Solution(object):
    def swapNumbers(self, numbers):
        """
        :type numbers: List[int]
        :rtype: List[int]
        """
        # [a, b] => [a ^ b, b]
        numbers[0] ^= numbers[1]
        # [a ^ b, b] => [a ^ b, a ^ b ^ b]= [a ^ b, a]
        numbers[1] ^= numbers[0]
        # [a ^ b, a] =>[a ^ b ^ a, a] = [b, a]
        numbers[0] ^= numbers[1]

        return numbers

    def swapNumbers2(self, numbers):
        # [a, b] => [a - b, b]
        numbers[0] -= numbers[1]
        # [a - b, b] => [a - b, b + (a - b)] = [a - b, a]
        numbers[1] += numbers[0]
        # [a - b, a] => [a - (a - b), a] = [b, a]
        numbers[0] = numbers[1] - numbers[0]

        return numbers


s = Solution()
print(s.swapNumbers2([3, 2]))