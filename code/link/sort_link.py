# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:  # 当只有一个节点时直接返回
            return head

        fast, slow = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        next_node = slow.next
        slow.next = None  # 要把链表一分为二

        left = self.sortList(head)
        right = self.sortList(next_node)

        return self.merge_sort(left, right)

    def merge_sort(self, left, right):
        head = ListNode(-10000)
        cur = head

        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
                cur = cur.next  # 需要移动
            else:
                cur.next = right
                right = right.next
                cur = cur.next

        cur.next = left if left else right

        return head.next