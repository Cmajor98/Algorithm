#  p——price每个物品的价值， w——weight每个物品的重量
def greedy(items, knapsacks):
    list = []   # 每个物品存放在的背包的编号
    itemsPW = []   # 每个物品的单位价值
    knapsacksC = knapsacks.copy()
    totalValue = 0  # 总价值
    for i in range(len(items)):
        p, w = items[i]
        pw = p / w   # 计算单位价值
        itemsPW.append((pw, p, w))
        list.append(-1)
    itemsPW.sort(reverse=True) # 单位价值从大到小排列
    for i in range(len(itemsPW)):
        for j in range(len(knapsacksC)):
            pw, p, w = itemsPW[i]
            if w < knapsacksC[j]:
                knapsacksC[j] -= w
                list[i] = j
                totalValue += p
                break
    return itemsPW, knapsacks, list, knapsacksC, totalValue

def neighbor_search(itemsPW, knapsacks, list, knapsacksC, totalValue):
    itemsLength = len(items)
    empty = []  # 未放入背包的物品
    # 第一阶段，通过交换已经放入背包的物品给外面的物品增加空间
    for j in range(itemsLength):
        if list[j] == -1: continue
        for k in range(j + 1, itemsLength):
            if list[k] == -1 or list[k] == list[j]: continue  # 判断是否在同一个包里
            pwj, pj, wj = itemsPW[j]
            pwk, pk, wk = itemsPW[k]
            if wj >= wk:
                m = j
                n = k
            else:
                m = k
                n = j
            d = abs(wj - wk)

            maxValue = 0
            t = -1
            wt = -1
            for i in range(len(itemsPW)):
                if list[i] == -1:
                    pwi, pi, wi = itemsPW[i]
                    empty.append(wi)
                    if wi <= knapsacksC[list[m]] + d and maxValue < pi:
                        maxValue = pi
                        t = i
                        wt = wi
            # 判断是否满足交换条件
            if d > knapsacksC[list[n]] or knapsacksC[list[m]] + d < min(empty): continue # 没有足够的容量用于交换时
            knapsacksC[list[m]] = (knapsacksC[list[m]] + d - wt)
            knapsacksC[list[n]] = (knapsacksC[list[n]] - d)
            list[t] = list[m]
            list[m] = list[n]
            list[n] = list[t]
            totalValue += maxValue

    # 第二阶段，通过丢弃背包里的物品给外面的物品留空间

    # 对每一个物品遍历，查找可以交换的物品
    for j in range (itemsLength):
        if list[j] == -1: continue
        pwj, pj, wj = itemsPW[j]
        for k in range(itemsLength):
            capacity = knapsacksC[list[j]] + wj # 把item 移走
            newList = set()

            pwk, pk, wk = itemsPW[k]
            if list[k] == -1 and wk <= capacity:  # 检查外面的物品是否可以放进
                newList.add(k)
                capacty = capacity - wk
            valueK = 0
            for k in newList:
                pwk, pk, wk = itemsPW[k]
                valueK += pk
            if valueK > pj:
                for k in newList:
                    list[k] = list[j]
                    knapsacksC[list[j]] = capacity
                    list[j] = -1
                    totalValue += (valueK- pj)
    return totalValue, list


items = [(30,40), (20,10), (80,40), (60,40), (60,50), (20,20)]
knapsacks = [100, 60]
itemsPw, knapsacks, list, knapsacksC, totalValue = greedy(items, knapsacks)
print("每个物品的单位价值：", itemsPw)
print("每个背包剩余的容量：", knapsacksC)
print("每个物品经过贪心算法放入的背包编号：", list)
print("经过贪心算法后的总价值：", totalValue)

totalValue2, list2 = neighbor_search(itemsPw, knapsacks, list, knapsacksC, totalValue)
print("经过邻域搜索后各物品放入的背包编号：", list2)
print("经过邻域搜索后的总价值：", totalValue2)
