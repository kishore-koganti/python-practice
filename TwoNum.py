from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            diff = target - num
            print("diff:" , diff)
            if diff in m:
                return [m[diff], i]
            print("num" , num)
            m[num] = i
            print(m[num])
        return []
    
sol_instance = Solution()
print(sol_instance.twoSum(nums=[2, 7, 11, 15], target=18))