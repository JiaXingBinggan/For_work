from base_data_stracture.stack import Stack

def post_fix_eval(expr): # 后缀表达式求值
    operateNumStack = Stack()
    token_list = expr.split()
    print(token_list)
    for token in token_list:
        if token in '0123456789':
            operateNumStack.push(token)
        elif token in '*/+-':
            operation2 = operateNumStack.pop()
            operation1 = operateNumStack.pop()
            new_operation = math_function(token, int(operation1), int(operation2))
            operateNumStack.push(str(new_operation))

    return operateNumStack.pop()

def math_function(token, operation1, operation2):
    if token == '*':
        return operation1 * operation2
    elif token == '/':
        if operation2 == 0:
            return 'NAN'
        else:
            return int(operation1 / operation2)
    elif token == '+':
        return operation1 + operation2
    else:
        return operation1 - operation2

print(post_fix_eval('9 3 + 3 / 4 1 - 1 3 + * -'))