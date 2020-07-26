class Solution:
    def moveTower(self, height, fromTower, withTower, toTower):
        '''
        :param height: 汉罗塔高度
        :param fromTower: 开始柱
        :param withTower: 中间柱
        :param toTower: 目标柱
        :return:
        '''
        if height >= 1:
            print('1', height-1, 'from', fromTower, 'with', toTower, 'to', withTower)
            self.moveTower(height - 1, fromTower, toTower, withTower) # 首先将上面N-1个盘片，从开始柱经由目标柱，移动到到中间柱
            self.moveDisk(height, fromTower, toTower) # 然后移动第N个盘片，从开始柱直接到目标柱
            print('2',height-1,  'from', withTower, 'with', fromTower, 'to', toTower)
            self.moveTower(height - 1, withTower, fromTower, toTower)  # 最后移动剩余N-1个盘片，经由开始柱，移动到目标柱

    def moveDisk(self, disk, fromTower, toTower):
        print('move disk {0}, from {1} to {2}'.format(disk, fromTower, toTower))

s = Solution()
s.moveTower(3, '#1', '#2', '#3')