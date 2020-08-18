# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def get_median(left, right):  # 链表求中点的方法，快慢指针
            fast, slow = left, left  # 快慢指针
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next

            return slow

        def build_bst(left, right):
            if left == right:
                return None
            mid = get_median(left, right)
            root = TreeNode(mid.val)
            root.left = build_bst(left, mid)  # 注意是mid
            root.right = build_bst(mid.next, right)  # 注意是next
            return root

        return build_bst(head, None)
