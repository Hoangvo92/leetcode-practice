#Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.

class Solution:
     
	def minSwaps(self, nums):
		#Code here
		if len(nums) < 1:
		    return 0
		sortArray = sorted(nums)
		odd = dict()
		savedID = list()
		savedNum = list()
		for i in range(0, len(nums)-1):
		    if sortArray[i]!=nums[i]:
		        odd[nums[i]] = i

		import collections
		od = collections.OrderedDict(sorted(odd.items()))
		for k, v in od.items():
		    savedID.append(v)
        if len(savedID)==0:
            return 0
		idMin = savedID[0]
        sumC = 0
		while (len(savedID)!= 0):
		
		    if idMin != 0:
		        sumC += 1
	
		    curr = savedID[0]
	
		    if curr > idMin:
		        curr -= 1
		    idMin = curr
		    savedID.pop()

		#sumC = minSort(nums, minNum, idMin, savedID, savedNum, sumC)
		return sumC
    
 	
		        



#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends







def minSwaps(arr):
    n = len(arr)
     
    # Create two arrays and use 
    # as pairs where first array 
    # is element and second array
    # is position of first element
    arrpos = [*enumerate(arr)]
     
    # Sort the array by array element 
    # values to get right position of 
    # every element as the elements 
    # of second array.
    arrpos.sort(key = lambda it : it[1])
     
    # To keep track of visited elements. 
    # Initialize all elements as not 
    # visited or false.
    vis = {k : False for k in range(n)}
     
    # Initialize result
    ans = 0
    for i in range(n):
         
        # alreadt swapped or 
        # alreadt present at 
        # correct position
        if vis[i] or arrpos[i][0] == i:
            continue
             
        # find number of nodes 
        # in this cycle and
        # add it to ans
        cycle_size = 0
        j = i
         
        while not vis[j]:
             
            # mark node as visited
            vis[j] = True
             
            # move to next node
            j = arrpos[j][0]
            cycle_size += 1
             
        # update answer by adding
        # current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
             
    # return answer
    return ans

 #https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/