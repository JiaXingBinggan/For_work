from base_data_stracture.queue import Queue
import random

random.seed(2020)

class Printer:
    def __init__(self, ppm): # 初始化打印器
        self.pagerate = ppm # 打印速度，每分钟打印多少页
        self.currentTask = None # 当前任务，传入的是“打印任务”对象
        self.timeRemaining = 0 # 任务倒计时

    def tick(self): # 每秒打印1次
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1 # 有打印任务时，每次打印1秒
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None: # 如果打印机内有打印任务，则忙
            return True
        else:
            return False

    def startNext(self, newStack):
        self.currentTask = newStack
        self.timeRemaining = newStack.getPages() * 60 / self.pagerate # newStack.getPages() / self.pagerate 获取到平均要打印多少秒

class Task: # 需要打印的任务的对象
    def __init__(self, time):
        self.timestamp = time # 记录任务创建时的时间戳
        self.pages = random.randrange(1, 21) # 随机生成需要打印的页数

    def getStamp(self):
        return self.timestamp # 返回创建时间戳

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime): # 计算当前任务已等待时间
        return currentTime - self.timestamp

def newPrintTask(): # 以1/180的概率生成打印任务
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False
'''
:param numSeconds-打印时间长度，例如3600（一个小时）,pagesPerMinute-每分钟打印多少页
'''
def simulation(numSeconds, pagesPerMinute):
    labPrinter = Printer(pagesPerMinute) # 初始化
    printQueue = Queue() # 打印任务队列
    waitingTimes = [] # 记录打印任务的等待时间

    for currentSecond in range(numSeconds): # 时间一秒一秒流逝
        if newPrintTask():
            newTask = Task(currentSecond)
            printQueue.enqueue(newTask) # 有新的任务进来，则首先进入队列

        if (not labPrinter.busy()) and (not printQueue.isEmpty()): # 当打印机不忙且任务队列不为空时，则开始新的打印任务
            nextTask = printQueue.dequeue() # 取出队首任务
            waitingTimes.append(currentSecond - nextTask.getStamp())
            labPrinter.startNext(nextTask)

        labPrinter.tick() # 每秒运行一次

    averageWaitTime = sum(waitingTimes) / len(waitingTimes)
    print('Average Wait {0} seconds, and {1} tasks remaining.'.format(averageWaitTime, printQueue.size()))

for i in range(10):
    simulation(3600, 10)