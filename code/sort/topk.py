'''
求数组里面最小的k个数
代码是快排解法，也可以使用堆排序解法
'''

def quick_index(nums, first, last):
    mid_num = nums[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while (left_mark <= right_mark and nums[left_mark] <= mid_num):
            left_mark += 1

        while (right_mark >= left_mark and nums[right_mark] >= mid_num):
            right_mark -= 1

        if left_mark > right_mark:
            done = True
        else:
            nums[left_mark], nums[right_mark] = nums[right_mark], nums[left_mark]

    nums[right_mark], nums[first] = mid_num, nums[right_mark]

    return right_mark


def min_num(array, m):
    start, end = 0, len(array) - 1
    index = quick_index(array, start, end)
    while index != m:
        if index < m:
            index = quick_index(array, index+1, end)
        else:
            index = quick_index(array, start, index)

    print(array[:m]) # 如果是最大的数，则需要反过来取

def max_num(array, m):
    start, end = 0, len(array) - 1
    index = quick_index(array, start, end)

    while len(array) - index != m:
        if len(array) - index < m: # 说明不够，需要向左取
            index = quick_index(array, start, index - 1) # 和min_num是反着来的
        else:
            index = quick_index(array, index + 1, end)

    print(array[-m:])

if __name__ == '__main__':
    alist = [15,54, 26, 93, 17, 77, 31, 44, 55, 20]

    min_num(alist,  5)

    max_num(alist, 5)