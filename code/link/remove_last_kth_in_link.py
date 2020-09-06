'''
题目描述
给定一个链表，删除链表的倒数第n个节点并返回链表的头指针
例如，

 给出的链表为:1->2->3->4->5, n= 2.
 删除了链表的倒数第n个节点之后,链表变为1->2->3->5.

'''
class Solution:
    def removeNthFromEnd(self, head, n):
        # write code here
        if not head:
            return head

        pre, slow, fast = None, head, head

        i = 0
        while fast and i < n:
            fast = fast.next
            i += 1

        if not fast: # 刚好列表长度等于n，则只用去除第一位
            return head.next

        while fast:
            fast = fast.next
            pre = slow
            slow = slow.next

        pre.next = slow.next

        return head
