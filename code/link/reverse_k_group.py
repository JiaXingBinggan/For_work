# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def reverseKGroup(self, head, k):
        # write code here
        if not head:
            return head

        def swap(head, final):
            pre = None
            cur = head

            while cur != final:
                cur.next, pre, cur = pre, cur, cur.next

            return pre

        if k == 1:
            return head

        cur, tail = head, head

        for i in range(k):
            if not tail: return head
            tail = tail.next

        new_cur = swap(cur, tail) # 反转当前cur和tail，顺序交换，cur变为尾结点
        cur.next = self.reverseKGroup(tail, k) # 反转后，将尾节点的next指针指向下一段的头结点

        return new_cur