class HashTable:
    '''
    实现ADT Map，散列类型，实现o(1)的查找时间复杂度
    '''
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash(self, key):
        '''
        散列函数，计算散列值
        :param item: 原始数值
        :return:
        '''
        return key % self.size

    def rehash(self, pos):
        '''
        再散列函数，计算新的散列值
        :param pos: 原始数据的原始散列值
        :return:
        '''
        return (pos + 1) % self.size

    def put(self, key, value):
        '''
        新增key-value键值对，如果存在则更新
        :param key:
        :param value:
        :return:
        '''
        hashvalue = self.hash(key)

        if self.slots[hashvalue] == key: # 首先比对是否存在key，如果存在则更新
            self.values[hashvalue] = value
        else:
            if self.slots[hashvalue] == None:
                self.slots[hashvalue] = key
                self.values[hashvalue] = value
            else:
                next_pos = self.rehash(hashvalue)
                while self.slots[next_pos] != None and self.slots[next_pos] != key: # 线性探测解决散列冲突，直到找到空槽，或者找到key
                    next_pos = self.rehash(next_pos)

                if self.slots[next_pos] == None:
                    self.slots[next_pos] = key
                    self.values[next_pos] = value
                else:
                    self.values[next_pos] = value

    def get(self, key):
        '''
        根据key，查询value
        :param key:
        :return:
        '''
        found = False # 用于判断是否找到
        stop = False # 用于判断是否停止，也就是循环了一圈也没有找到
        startslot = self.hash(key) # 初始位置

        position = startslot

        while self.slots[position] != None and not found and not stop:
            # 线性探测查找判断，如果从初始位置出发，遇到了一个None，还是没找到key的话，则说明该散列表中没有key，则可提前结束
            if self.slots[position] == key:
                found = True
                return self.values[position]
            else:
                position = self.rehash(position)
                if position == startslot: # 循环一圈，没找到即退出
                    stop = True

        return found

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

h = HashTable()
h[54] = 'test'
print(h.get(54))
print(h.slots)
print(h.values)

