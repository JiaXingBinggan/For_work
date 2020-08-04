# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    # 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
    def Merge(self, pHead1, pHead2):
        # write code here
        new_head = ListNode(-10000)
        cur = new_head
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                cur.next = ListNode(pHead1.val)
                pHead1 = pHead1.next
            else:
                cur.next = ListNode(pHead2.val)
                pHead2 = pHead2.next

            cur = cur.next

        cur.next = pHead1 if pHead1 else pHead2

        return new_head.next
