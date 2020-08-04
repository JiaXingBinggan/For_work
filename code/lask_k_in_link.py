# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，
        本题从1开始计数，即链表的尾节点是倒数第1个节点。
        例如，一个链表有6个节点，从头节点开始，
        它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        # 列表翻转思路
        re_head = self.reverseLink(head)
        i = 1
        cur = re_head
        while i < k:
            cur = cur.next
            i += 1
        cur.next = None

        return self.reverseLink(re_head)

    def reverseLink(self, head):
        pre = None
        cur = head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next

        return pre

class Solution2(object):
    def getKthFromEnd(self, head, k):
        """
        输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，
        本题从1开始计数，即链表的尾节点是倒数第1个节点。
        例如，一个链表有6个节点，从头节点开始，
        它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 双指针思路
        latter, former = head, head
        for i in range(k):
            former = former.next

        while former:
            latter = latter.next
            former = former.next

        return latter

