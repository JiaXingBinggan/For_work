# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        queue = [root]  # 用于存放

        res_list = [root.val]
        while len(queue) > 0:
            current_node = queue.pop(0)

            if current_node.left:
                queue.append(current_node.left)
                res_list.append(current_node.left.val)
            else:
                res_list.append('null')

            if current_node.right:
                queue.append(current_node.right)
                res_list.append(current_node.right.val)
            else:
                res_list.append('null')

        still_null = True
        for res in reversed(res_list):
            if res == 'null':
                if still_null:
                    res_list.pop()
            else:
                still_null = False
        res_str = '['
        for i, res in enumerate(res_list):
            res_str += str(res)
            if i != len(res_list) - 1:
                res_str += ','
        res_str += ']'

        return res_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0: return
        data = data[1:-1].split(',')
        root = TreeNode(data[0])
        queue = [root]  # 用于控制当前root节点

        return_tree = root

        i = 1

        while len(queue) > 0 and i < len(data):
            current_node = queue.pop(0)  # 当前节点
            if not current_node.left and not current_node.right:
                new_node = TreeNode(data[i])
                current_node.left = new_node
                i += 1
                queue.insert(0, current_node)
                queue.append(current_node.left)
            elif current_node.left and not current_node.right:
                new_node = TreeNode(data[i])
                current_node.right = new_node
                i += 1
                queue.append(current_node.right)

        return return_tree

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

s = Solution()
root = s.deserialize("[1,null,2]")
print(s.serialize(root))