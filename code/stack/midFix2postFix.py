from base_data_stracture.stack import Stack

'''
中缀表达式转后缀表达式算法
例如：( A + B ) * C, ( A + B ) * C - ( D - E ) * ( F + G )
'''
def midfix2postfix(expr):
    priorities = {}
    priorities['*'] = 3
    priorities['/'] = 3
    priorities['+'] = 2
    priorities['-'] = 2
    priorities['('] = 1

    opStack = Stack() # 用来存储操作的栈
    post_fix_list = list() # 用来存储后缀表达式的操作数和操作符
    tokenlist = expr.split() # 把中缀表达式转为list
    print(tokenlist)
    for token in tokenlist:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            post_fix_list.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            top_stack = opStack.pop()
            # 当扫描到右括号时，如果栈顶不是左括号，则一直弹栈（因为里面都是优先级由高到低的操作符），知道栈顶是左括号为止
            while top_stack != '(':
                post_fix_list.append(top_stack)
                top_stack = opStack.pop()
        else:
            # 当token是*/+-时，则判断栈是否为空，并且判断栈顶的优先级是否高于当前token的优先级，
            # 高于则弹栈并把栈顶置于后缀表达式中，不高则把当前token置于后缀表达式中
            # 最后把当前token置于栈顶
            while not opStack.isEmpty() and priorities[opStack.peek()] >= priorities[token]:
                post_fix_list.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty(): # 有可能还有些优先级较低的操作符，全部弹出并置于后缀表达式中
        post_fix_list.append(opStack.pop())

    return "".join(tuple(post_fix_list))

print(midfix2postfix('( A + B ) * C'))
print(midfix2postfix('( A + B ) / C - ( D - E ) * ( F + G )'))
print(midfix2postfix('( 1 + ( 4 * 5 + 2 ) - 3 ) + ( 6 + 8 )'))