import random
import time
start = time.clock()

def merge_Sort(lists):
    if len(lists)<=1:
        return lists
    else:
        mid=len(lists)//2
        AL=lists[0:mid]
        AR=lists[mid:]
        S_AL=merge_Sort(AL)
        S_AR=merge_Sort(AR)
        return merge(S_AL,S_AR)

def merge(S_AL,S_AR):
    i,j=0,0
    result=[]
    while i<len(S_AL) and j<len(S_AR):
        if S_AL[i]<=S_AR[j]:
            result.append(S_AL[i])
            i+=1
        else:
            result.append(S_AR[j])
            j+=1
    result+=S_AL[i:]
    result+=S_AR[j:]
    return result

if __name__=="__main__" :
    A = [random.randint(0, 1000) for _ in range(1000)]
    iniTime = time.clock()
    #print(A)
    #merge_Sort(A)
    print(merge_Sort(A))
    end = time.clock()
    print('Algorithm initializing time: %s seconds' % (iniTime - start))
    print('Mergesort Running time: %s seconds' % (end - iniTime))
    print('Total running time: %s seconds' % (end - start))