///week04-1
///LeetCode 2579. Count Total Number of Colored Cells
class Solution:
    def coloredCells(self, n: int) -> int:
        ans=0 #迴圈前面, ans 先清空
        for i in range(1, n*2, 2): #Python 的 for 迴圈
            ans += i # 把這些1,3,5,7的數,加入ans
        for i in range(1, n*2-1, 2):
            ans += i # 把這些1,3,5,的數,加入ans
        return ans

