# -*- coding: utf-8 -*-

def findLength(nums1, nums2) -> int:
    n = len(nums1)
    m = len(nums2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    res = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if nums1[i-1] == nums2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])

    print(dp)
    return res


if __name__ == "__main__":
    nums1 = [1,2,3,2,1]
    nums2 = [3,2,1,4,7]
    res = findLength(nums1, nums2)
    print(res)
