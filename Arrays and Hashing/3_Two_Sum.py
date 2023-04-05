'''
Given an array of numbers and a target number
Return the indices of two numbers such that they add up to target
You may not use the same element twice
There should be only one solution
'''

'''
Initial Thought Process
We do a really funny O(n^2) algorithm where we go down every index and check every other index for the answer
'''

'''
Potential answer
We go down each index once and put the number and the number needed to 
'''

def twoSum(nums: list[int], target: int):
    storage = {}
    for i in range(len(nums)):
        storage[target - nums[i]] = i
    
    for i in range(len(nums)):
        if storage[nums[i]] == None:
            continue
        if storage[nums[i]] != i:
            return sorted([storage[nums[i]], i])
    
    return False

print(twoSum([2,7,11,15], 9))

# O(n) before sorting, O(nlogn) after sorting