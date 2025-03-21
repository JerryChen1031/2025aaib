
#week02-3.py 寫 LeetCode
#LeetCode 1. Two Sum
#有一堆數字 nums裡面[哪兩個]相加,是 tatget
#nums[i] + nums[j] == target 找到 i 和 j 使得加起來是 target
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        box = {} # 有一個箱子, 裡面放[出現過的數字]
        # 我們想要湊出target 這個加總

        for i, num in enumerate(nums):
            other = target - num
            if other in box:
                return[ box[other], i ]
            else:
                    box[num] = i
