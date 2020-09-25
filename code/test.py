class Solution:
    def kthFactor(self, n):
        forward = []
        backward = []

        middle = int(n**0.5)
        for i in range(1,middle+1):
            if n % i == 0:
                forward.append(i)
                if i == int(n/i):
                    break
                backward.append(int(n/i))

        return forward + backward[::-1]

s = Solution()
print(s.kthFactor(16))