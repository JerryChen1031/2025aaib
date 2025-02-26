
#week02-3.py �g LeetCode
#LeetCode 1. Two Sum
#���@��Ʀr nums�̭�[�����]�ۥ[,�O tatget
#nums[i] + nums[j] == target ��� i �M j �ϱo�[�_�ӬO target
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        box = {} # ���@�ӽc�l, �̭���[�X�{�L���Ʀr]
        # �ڭ̷Q�n��Xtarget �o�ӥ[�`

        for i, num in enumerate(nums):
            other = target - num
            if other in box:
                return[ box[other], i ]
            else:
                    box[num] = i
