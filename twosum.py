#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].


#Hint:
#Enumerate is a built-in function of Python. Its usefulness can not be summarized in a single line. Yet most of the newcomers and even some advanced programmers are unaware of it. It allows us to loop over something and have an automatic counter. Here is an example:

#for counter, value in enumerate(some_list):
#    print(counter, value)


class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        checker = {}
        for i, v in enumerate(nums):
            if target - v in checker:
                return [checker[target - v], i]
            else:    
                checker[v] = i
        return []  
