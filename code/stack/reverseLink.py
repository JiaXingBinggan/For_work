class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        stack = [head.val] # 利用栈存储当前顺序值，反转后即成为了倒序。看到反转顺序的都可以考虑栈
        while head.next:
            stack.insert(0, head.next.val)
            head = head.next

        new_head = ListNode(stack.pop(0))
        temp_head = new_head
        while len(stack) > 0:
            current_val = stack.pop()
            current_node = ListNode(current_val)
            current_node.next = temp_head.next
            temp_head.next = current_node

        return new_head