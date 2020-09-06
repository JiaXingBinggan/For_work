class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param head1 ListNode类
# @param head2 ListNode类
# @return ListNode类
#

'''
假设链表中每一个节点的值都在 0 - 9 之间，那么链表整体就可以代表一个整数。
给定两个这种链表，请生成代表两个整数相加值的结果链表。
例如：链表 1 为 9->3->7，链表 2 为 6->3，最后生成新的结果链表为 1->0->0->0。 
'''
class Solution:
    def addInList(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        r_head1, r_head2 = self.reverseLink(head1), self.reverseLink(head2)

        res = ListNode(-1000)
        res_link = res
        is_up = 0
        while r_head1 or r_head2 or is_up:
            current_add = is_up + (r_head1.val if r_head1 else 0) + (r_head2.val if r_head2 else 0)
            is_up = current_add // 10
            res_link.next = ListNode(current_add % 10)
            res_link = res_link.next
            r_head1 = r_head1.next if r_head1 else None
            r_head2 = r_head2.next if r_head2 else None

        return self.reverseLink(res.next)

    def reverseLink(self, head):
        pre = None
        cur = head

        while cur:
            cur.next, pre, cur = pre, cur, cur.next

        return pre