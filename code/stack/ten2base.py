from base_data_stracture.stack import Stack

def ten2base(num, base): # 十进制转N进制，除以N取余数，置于栈底
    digits = '0123456789ABCDEF'
    # 为了适应16进制，因为二进制，8进制都包含在16进制的编码以内；甚至可以在F后面再加以达到更高进制的转换

    stack = Stack()

    while num != 0:
        stack.push(num % base)
        num = num // base

    two_str = ''
    while not stack.isEmpty():
        two_str += str(digits[stack.pop()])

    return two_str

print(ten2base(35, 2)) # 转为二进制
print(ten2base(35, 8)) # 转为八进制
print(ten2base(35, 16)) # 转为十六进制
