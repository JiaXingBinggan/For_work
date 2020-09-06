# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

        如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

        您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

        示例：

        输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
        输出：7 -> 0 -> 8
        原因：342 + 465 = 807


        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        r_l1, r_l2 = l1, l2

        res = ListNode(-1000)
        res_link = res
        is_up = 0
        while r_l1 or r_l2 or is_up:
            current_add = is_up + (r_l1.val if r_l1 else 0) + (r_l2.val if r_l2 else 0)
            is_up = current_add // 10
            res_link.next = ListNode(current_add % 10)
            res_link = res_link.next
            r_l1 = r_l1.next if r_l1 else None
            r_l2 = r_l2.next if r_l2 else None

        return res.next

head1 = ListNode(3)
cur = head1
cur.next = ListNode(4)
cur = cur.next
cur.next = ListNode(5)
head2 = ListNode(2)
cur = head2
cur.next = ListNode(3)

s = Solution()
r = s.addTwoNumbers(head1, head2)
while r:
    print(r.val)
    r = r.next