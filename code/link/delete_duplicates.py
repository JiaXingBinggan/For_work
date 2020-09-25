# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2

示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        pre = head # 双指针法，先固定一个节点
        cur = head # 然后用当前节点去遍历
        while cur:
            if cur.val != pre.val: # 如果出现新值，则把此前的pre节点的next指向cur节点（相当于删除重复值）
                pre.next = cur
                pre = cur
            cur = cur.next
        pre.next = None # 最后需要单独指向None（因为有可能存在1->1->2->3->3的情况，在末尾时没有出现新值，如果不单独指向则无法去除重复节点）
        return head
