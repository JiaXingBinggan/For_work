from base_data_stracture.stack import Stack

def parChecker(pars): # 同时存在多种不同的开闭符号的符号匹配
    stack = Stack()
    isBalanced = True
    par_index = 0
    while par_index < len(pars) and isBalanced:
        if pars[par_index] in '([{':
            stack.push(pars[par_index])
        else:
            if stack.isEmpty():
                isBalanced = False
            else:
                topStack = stack.pop() # 返回栈顶符号
                isBalanced = match(topStack, pars[par_index])

        par_index += 1

    if stack.isEmpty() and isBalanced: # 栈为空的话，则表明已经匹配完成（但需要加个限制条件，要匹配才行，例如(}这样的组合）
        return True
    else:
        return False

def match(top, symbol):
    left_symbols = '([{'
    right_symbols = ')]}'

    return left_symbols.index(top) == right_symbols.index(symbol)
    # 这里有个技巧，就是按照对应顺序，例如左括号则对应右括号的位置，
    # 例如left_symbols的左括号位置是0，right_symbols的右括号位置是0，如果top和symbol能够一一对应，则证明匹配成功

print(parChecker('{{[[()]()]}}'))
print(parChecker('{{[[(])()]}}'))