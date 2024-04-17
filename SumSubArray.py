from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> int:
        m = []
        for i, num in enumerate(nums):
            print("sum..", sum(m))
            if sum(m) == target:
                return i
            print("num" , num)
            m.append(num)
            print(m[i])
        return []
    
sol_instance = Solution()
print("value:: " , sol_instance.twoSum(nums=[1,2,1,2,1], k=3))