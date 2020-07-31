# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        final_node = ListNode(-10000)
        return_node = final_node
        # 思路和归并排序一样，交错比较
        while l1 and l2:
            if l1.val <= l2.val:
                return_node.next, l1 = l1, l1.next
            else:
                return_node.next, l2 = l2, l2.next
            return_node = return_node.next

        return_node.next = l1 if l1 else l2

        return final_node.next