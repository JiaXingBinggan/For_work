# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mid_link(self, head):
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

        return slow