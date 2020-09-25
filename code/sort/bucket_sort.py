class Solution:
    def bucket_sort(self, list):
        '''
        桶排序
        :param list:
        :return:
        '''
        min_value, max_value = min(list), max(list)
        if min_value < 0: # 存在负数的处理
            max_len = max_value - min_value + 1 # 要包括1
        else:
            max_len = max_value + 1 # 要包括1

        buckets = [0 for _ in range(max_len)] # 用生成器的方法来建立列表

        for value in list:
            buckets[value - min_value] += 1

        res = []

        for i, count in enumerate(buckets):
            for _ in range(count):
                res.append(i + min_value)

        return res

    def bucket_sort1(self, list):
        if not list:
            return list
        max_value, min_value = max(list), min(list)

        if min_value < 0:
            max_len = max_value - min_value + 1
        else:
            max_len = max_value + 1

        buckets = [0 for _ in range(max_len)]

        for value in list:
            buckets[value - min_value] += 1

        res = []
        for i, count in enumerate(buckets):
            for _ in range(count):
                res.append(i + min_value)

        return res

    # 可对小数排序
    def bucket_sort2(self, arr):
        if not arr:
            return False
        # 保留两位小数
        accuracy = 100.
        offset = int(min(arr) * accuracy)
        max_len = int(max(arr) * accuracy - offset + 1)
        book = [0 for x in range(0, max_len)]
        for i in arr:
            book[int(i * accuracy - offset)] += 1
        return [(i + offset) / accuracy for i in range(0, max_len) for j in range(0, book[i])]

s = Solution()
print(s.bucket_sort([-3,-5,3,4,2,6,5,8]))
print(s.bucket_sort1([-3,-5,3,4,2,6,5,8]))

