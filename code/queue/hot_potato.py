from base_data_stracture.queue import Queue

def hot_potato(a_list, num): # 热土豆问题，一群人传递土豆，当传递num次后，拿到土豆的人出列，直至剩下一个人
    queue = Queue()
    for a in a_list:
        queue.enqueue(a) # 入列

    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue()) # 把队首添加至队尾，即发生了一次传递

        queue.dequeue() # 当传递了num次后则队首出列（即拿到土豆的那个人出列）

    return queue.dequeue()

print(hot_potato(list('abcdef'), 7))