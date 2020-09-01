'''
寻找数组中第k大的元素

快速排序使用了分治法的策略。它的基本思想是，选择一个基准数（一般称之为枢纽元），通过一趟排序将要排序的数据分割成独立的两部分：在枢纽元左边的所有元素都不比它大，右边所有元素都比它大，此时枢纽元就处在它应该在的正确位置上了。在本问题中，假设有N个数存储在数组a中。

我们从a中随机找出一个元素作为枢纽元，把数组分为两部分。其中左边元素都不比枢纽元大，右边元素都不比枢纽元小。此时枢纽元所在的位置记为mid。

    如果右半边（包括a[mid]）的长度恰好为k，说明a[mid]就是需要的第k大元素，直接返回a[mid]。
    如果右半边（包括a[mid]）的长度大于k，说明要寻找的第k大元素就在右半边，往右半边寻找。
    如果右半边（包括a[mid]）的长度小于k，说明要寻找的第k大元素就在左半边，往左半边寻找。

'''

def partition(nums, first, last):
    mid_num = nums[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and nums[left_mark] <= mid_num:
            left_mark += 1

        while right_mark >= left_mark and nums[right_mark] >= mid_num:
            right_mark -= 1

        if left_mark > right_mark:
            done = True
        else:
            nums[left_mark], nums[right_mark] = nums[right_mark], nums[left_mark]

    nums[right_mark], nums[first] = mid_num, nums[right_mark]

    return right_mark

def quick(nums, left, right, k):
    low = partition(nums, left, right)
    if (len(nums) - low - 1) == k:
        return nums[low]
    elif (len(nums) - low - 1) < k:
        return quick(nums, low + 1, right, k)
    else:
        return quick(nums, left, low - 1, k)

num = [1,4,5,3,2,7,6]
k = 3
print(quick(num, 0, len(num) - 1, k))