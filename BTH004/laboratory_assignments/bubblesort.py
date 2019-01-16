import random
import time
start =time.clock()
def bubbleSort(bubbleList):
    n=len(bubbleList)
    while n>0:
        for i in range(n-1):
            if bubbleList[i] > bubbleList[i+1]:
                temp=bubbleList[i+1]
                bubbleList[i+1]=bubbleList[i]
                bubbleList[i]=temp
        n -= 1
    return bubbleList

if __name__ == '__main__':
    bubbleList = [random.randint(0, 10) for _ in range(10)]
    iniTime = time.clock()
    #print(bubbleList)
    #print(bubbleSort(bubbleList))
    print(bubbleSort(bubbleList))
    end = time.clock()
    print('Algorithm initializing time: %s seconds' % (iniTime - start))
    print('Mergesort Running time: %s seconds' % (end - iniTime))
    print('Total running time: %s seconds' % (end - start))