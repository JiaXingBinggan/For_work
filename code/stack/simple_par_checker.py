from base_data_stracture.stack import Stack

def par_checker(pars): # 简单括号匹配，具有最近匹配的特性的命题则可使用栈
    stack = Stack() # 初始化栈
    isBalanced = True # 是否匹配
    par_index = 0

    while par_index < len(pars) and isBalanced:
        if pars[par_index] == '(': # 是左括号，则push至栈顶
            stack.push(pars[par_index])
        else: # 是右括号，则要判断栈是否为空，不为空则pop栈顶
            if stack.isEmpty():
                isBalanced = False
            else:
                stack.pop()

        par_index += 1

    if stack.isEmpty() and isBalanced:
        return True
    else:
        return False

print(par_checker('((()))'))
print(par_checker('())'))


