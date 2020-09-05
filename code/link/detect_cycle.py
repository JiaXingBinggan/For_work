class Solution:
    def detectCycle(self, head):
        # write code here
        if not head:
            return head

        slow, fast = head, head

        while fast and fast.next: # 首先要判断是否有环，如果直接就遍历到None，则没环
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None