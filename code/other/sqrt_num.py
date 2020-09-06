import math
class Solution:
    def sqrtNum(self, num):
        '''
        不使用python自带函数来求num的平方根（保留小数位9位），该类题都可以使用二分法来求得
        首先得判断num左右两边的数能否进行平方
        以10为例，10的左边是9=3^2，右边是16=4^2，因此根号10只用在3-4的范围内进行寻找
        :param num:
        :return:
        '''
        epsilon = 1e-9
        first = 3
        last = 4
        mid = (first + last) / 2

        while last - first > epsilon: # 停止条件为first和last的差值小于epsilon
            if mid ** 2 > 10:
                last = mid
            else:
                first = mid

            mid = (first + last) / 2

        return mid

s = Solution()
print(s.sqrtNum(10), math.sqrt(10))

