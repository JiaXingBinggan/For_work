class Solution(object):
    def deleteNode(self, node):
        """
        实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），假定你只能访问该节点。
        示例：
        输入：单向链表a->b->c->d->e->f中的节点c
        结果：不返回任何数据，但该链表变为a->b->d->e->f
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val # 先将下一个节点的val赋值给当前node，即a->b->c->d->e->f变为a->b->d->d->e->f
        node.next = node.next.next # 然后把当前node的next指向下一个节点的next