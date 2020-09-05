class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        epsilon = 1

        first, last = 0, x # 因为平方根必定比x小，因此可以设置下界为0，上界为x
        mid = (first + last) / 2

        while first <= last:
            if mid ** 2 > x:
                last = mid - epsilon
            else:
                first = mid + epsilon
            mid = (first + last) / 2

        return int(mid)

    def mySqrt2(self, x):
        if x == 0:
            return 0

        epsilon = 1e-3

        first, last = 0, x
        mid = (first + last) / 2

        while (last - first) > epsilon:
            if mid ** 2 > x:
                last = mid - epsilon
            else:
                first = mid + epsilon
            mid = (first + last) / 2

        return int(mid)

