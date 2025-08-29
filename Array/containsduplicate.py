#https://leetcode.com/problems/contains-duplicate/
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
#2nd approch
#a=set(nums)
#return len(a)!=len(nums)
#3rd approch
#nums.sort()
#for i in range(1,len(nums)):
#    if nums[i]==nums[i-1]:
#        return True
#return False   

