# -*- coding: utf-8 -*-

def longestStrChain(words) -> int:
    # 特例
    if len(words) == 1:
        return 1

    # 常规
    def helper(prev, curr):
        # 1
        if len(prev)+1 != len(curr):  # 神来之笔
            return False
        # 2
        for i in range(len(curr)):
            tmp = curr[0:i] + curr[i+1:]  # 神来之笔
            if tmp == prev:
                return True
        return False

    n = len(words)
    words.sort(key=lambda x: len(x))
    dp = [1]*n

    for i in range(1, n):
        for j in range(0, i):
            curr = words[i]
            prev = words[j]
            flag = helper(prev, curr)

            if flag:
                dp[i] = max(dp[i], dp[j]+1)  # 神来之笔
                print(dp)

    return max(dp)


if __name__ == "__main__":
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    res = longestStrChain(words)
    print(res)
