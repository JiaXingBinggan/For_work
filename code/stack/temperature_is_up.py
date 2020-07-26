from base_data_stracture.stack import Stack

def temp_is_up(tempratures):
    low_temp_stack = Stack() # 单调栈

    up_days = [0] * len(tempratures)
    for i, temp in enumerate(tempratures, start=0):
        if low_temp_stack.isEmpty():
            low_temp_stack.push([temp, i])
        while not low_temp_stack.isEmpty() and temp > low_temp_stack.peek()[0]: # 在while循环外，temp始终是最大的，也就是栈内数据是由栈底到栈顶逐渐升高的，如果栈底最后没有遇到比它高的，肯定就没有升高
            top_stack = low_temp_stack.pop()
            up_days[top_stack[1]] = i - top_stack[1]
        low_temp_stack.push([temp, i])

    return up_days

print(temp_is_up([73, 74, 75, 71, 69, 72, 76, 73]))