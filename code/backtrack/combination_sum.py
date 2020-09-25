class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

        candidates 中的每个数字在每个组合中只能使用一次。

        说明：

            所有数字（包括目标数）都是正整数。
            解集不能包含重复的组合。

        示例 1:

        输入: candidates = [10,1,2,7,6,1,5], target = 8,
        所求解集为:
        [
          [1, 7],
          [1, 2, 5],
          [2, 6],
          [1, 1, 6]
        ]

        示例 2:

        输入: candidates = [2,5,2,1,2], target = 5,
        所求解集为:
        [
          [1,2,2],
          [5]
        ]
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return candidates

        candidates.sort()

        res = []

        def backtrack(track, choose_list):
            if sum(track) > target: # 剪枝
                return
            if sum(track) == target and track[:] not in res: # 剪枝
                res.append(track[:])
                return

            for i, choose in enumerate(choose_list):
                if choose_list[i] > target:
                    continue
                track.append(choose)
                backtrack(track, choose_list[i + 1:])
                track.pop()

        backtrack([], candidates)

        return res