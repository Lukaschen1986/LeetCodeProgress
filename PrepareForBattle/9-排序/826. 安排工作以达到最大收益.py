# -*- coding: utf-8 -*-
def maxProfitAssignment(difficulty, profit, worker):
    '''
    超时
    '''
    diff_profit = [(k, v) for (k, v) in zip(difficulty, profit)]
    diff_profit.sort(key=lambda x: x[0])
    n = len(diff_profit)
    worker.sort()
    total_profit = 0
    start = 0
    tmp = 0

    for w in worker:
        for i in range(start, n):
            if w >= diff_profit[i][0]:
                tmp = max(tmp, diff_profit[i][1])
                start = i
        total_profit += tmp
        
    return total_profit





if __name__ == "__main__":
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]  # 100
    
    difficulty = [85, 47, 57]
    profit = [24, 66, 99]
    worker = [40, 25, 25]  # 0
    
    difficulty = [13, 37, 58]
    profit = [4, 90, 96]
    worker = [34, 73, 45]  # 190

    difficulty = [68, 35, 52, 47, 86]
    profit = [67, 17, 1, 81, 3]
    worker = [92, 10, 85, 84, 82]  # 324
    
    res = maxProfitAssignment(difficulty, profit, worker)
    print(res)
