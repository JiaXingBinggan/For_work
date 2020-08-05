class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        输入两个链表，找出它们的第一个公共节点。
        https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA, curB = headA, headB

        while curA != curB: # 双指针交替遍历，以消除长度差距
            # https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solution/shuang-zhi-zhen-fa-lang-man-xiang-yu-by-ml-zimingm/
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA

        return curA