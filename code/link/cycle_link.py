# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        fast, slow = head.next, head

        while fast != slow:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next

        return True

    def hasCycle2(self, head):
        if not head:
            return False

        slow, fast = head, head.next

        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next

        return fast == slow