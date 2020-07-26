from base_data_stracture.stack import Stack

def ten2two(num): # 十进制转二进制，除以2取余数，置于栈底
    stack = Stack()

    while num != 0:
        stack.push(num % 2)
        num = num // 2

    two_str = ''
    while not stack.isEmpty():
        two_str += str(stack.pop())

    return two_str

print(ten2two(35))