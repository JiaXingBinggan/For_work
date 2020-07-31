# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        反转链表的不用栈的解法
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None # 因为要反转，所以需要把最后一个节点的next设为None，pre表示当前节点的前置节点
        cur = head
        while cur:
            temp = cur.next # 需要把next的指针情况保存下来，不然会出现找不到指针的问题
            cur.next = pre # 当前节点的next，反转指向pre节点
            pre = cur # pre设为当前节点
            cur = temp # cur设置原始cur的next节点
            # cur.next, pre, cur = pre, cur, cur.next

        return pre

    def reverseList2(self, head):
        """
        反转链表的不用栈的解法
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None # 因为要反转，所以需要把最后一个节点的next设为None，pre表示当前节点的前置节点
        cur = head
        while cur:
            # 注意这里的区别，和前面相比就是：Python多个变量同时赋值与多个变量分别单独赋值的不同
            # 多个变量同时赋值，等号后面的值是暂存在内存中的，因此可以直接复制
            # 然而多个变量单独赋值后，原始变量的值已经在内存中被替换，所以会被更改
            # https://blog.csdn.net/weixin_41606064/article/details/107370617?fps=1&locationNum=2
            cur.next, pre, cur = pre, cur, cur.next

        return pre # 注意这里需要返回pre，因为最后的时候pre赋值为了cur，而cur赋值给了cur.next