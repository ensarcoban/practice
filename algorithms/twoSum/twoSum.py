from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    Time complexity of this code is O(n^2). It does not use a lot of memory.
    Using a variable called result instead of reach nums[i] in second for loop everytime decrease runtime.
    """
    result = 0
    for i in range(len(nums)):
        result = nums[i]
        for j in range(i+1, len(nums)):
            if (target == (result+nums[j])):
                return [i, j]



def twoSum2(nums: List[int], target: int) -> List[int]:
    """
    Time Complexity of this code is O(n) and very time efficient compared to other algorithm.
    However it uses more memory since it stores all past values. If size of the array is large, it won't be memory efficient.
    """
    hash_map = {}
    
    for i in range(len(nums)):
        if (target - nums[i]) in hash_map:
            return [hash_map[target-nums[i]], i]
        hash_map[nums[i]] = i