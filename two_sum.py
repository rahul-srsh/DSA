class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}

        for i,n in enumerate(nums):
            a[nums[i]] = i 
        
        for index,item in enumerate(nums):
            diff = target - item
            if diff in a :
                if index == a[diff] :
                    continue
                if index < a[diff] :

                    return [index,a[diff]]
                else :
                    return [a[diff], index
