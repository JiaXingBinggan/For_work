from base_data_stracture.deque import Deque

def huiwen_word(str): # 回文词判断
    word_deque = Deque() # 初始化双端队列

    for word in list(str):
        word_deque.addRear(word)

    is_balance = True
    while word_deque.size() > 1 and is_balance: # size>1的原因是，无论回文词长度是奇数还是
        front_word, rear_word = word_deque.removeFront(), word_deque.removeRear()
        if front_word != rear_word:
            is_balance = False

    return is_balance

print(huiwen_word('aba'))
print(huiwen_word('acfga'))
print(huiwen_word('abcdefgfedcba'))

