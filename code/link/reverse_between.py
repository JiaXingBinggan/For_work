class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
#
# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类
#
class Solution:
    def reverseBetween(self, head, m, n):
        # write code here
        if not head:
            return head
        pre = ListNode(-10000) # 为了判断是否是中间开始reverse的
        cur1 = head
        for i in range(m - 1):
            pre = cur1
            cur1 = cur1.next

        cur2 = cur1
        for i in range(n - m): # 找到需要被转的结束节点
            cur2 = cur2.next

        tail = cur2.next
        cur2.next = None

        r_cur1 = self.reverse(cur1)

        r_cur1_1 = r_cur1
        while r_cur1_1.next:
            r_cur1_1 = r_cur1_1.next

        r_cur1_1.next = tail # 将被转部分的next指针指向预先设置好的尾部

        if pre.val == -10000: # 如果是从head就转，则直接返回被转的部分即可
            return r_cur1
        else:
            pre.next = r_cur1 # 否则，需要先把head到被转部分之间的指针指向被转的部分
            return head

    def reverse(self, head):
        pre = None
        cur = head

        while cur:
            cur.next, pre, cur = pre, cur, cur.next

        return pre

node = ListNode(1)
cur = node
arr = [2, 3, 4, 5]
for item in arr:
    cur.next = ListNode(item)
    cur = cur.next

s = Solution()
r = s.reverseBetween(node, 2, 4)
while r:
    print(r.val)
    r = r.next

node = ListNode(5)
r = s.reverseBetween(node, 1, 1)
while r:
    print(r.val)
    r = r.next

node = ListNode(3)
node.next = ListNode(5)
r = s.reverseBetween(node, 1, 2)
while r:
    print(r.val)
    r = r.next

