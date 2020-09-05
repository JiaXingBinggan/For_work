'''
 功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
最后一个数后面也要有空格

'''
if __name__ == '__main__':
    num = int(input())
    primes = []
    prime = 2 # 从2开始遍历，因为如果一个数能被偶数整除，则它肯定会被2整除，所以不用管prime+=1后遍历到4或者8，因为早已经被2给消化掉了
    while num >= prime: # 停止条件
        if num % prime == 0:
            primes.append(prime)
            num /= prime
        else:
            prime += 1
    primes.sort()
    if len(primes) == 1:
        print(str(primes[0]) + ' ')
    else:
        print(' '.join(list(map(str, primes))) + ' ')