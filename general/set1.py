# Find equilibrium index of an array: left and right sums are the same


def equilibriumIndex(arr):
    right = 0
    leftover = 0
    equilibIndex = 0
    total = sum(arr)
    for i in range(len(arr)-1, -1, -1):
        leftover = total - (arr[i] + right)
        right += arr[i]
        if right == leftover:
            return i


arr = [1, 2, 3, 5, 7, 9, 10, -1]
print(equilibriumIndex(arr))

# Given an array nums and a value val, remove all instances of that value in-place and return the new length.


def removeElement(self, nums: List[int], val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count


def isPalindrome(self, x: int) -> bool:
    return str(x) == str(x)[::-1]

# max profit k transactions

def maxProfitWithKTransactions(prices, k):
	# check for empty prices array
	if not len(prices): 
		return 0
	# create the 2D array of profits 
	profits = [[0 for d in prices] for t in range(k+1)]
	# iterate through the 2D array of profits
	# start with the rows
	for t in range(1, k + 1):
		# keep track of max profit from 1 transaction up to this point
		# initialize to the smallest possible value in Python
		maxThusFar = float("-inf")
		for d in range(1, len(prices)):
			# max of 
			# 1. do nothing, so get the previous day's profits
			# 2. sell, so get today's sell price + max profit from 1 transaction 
			# Keep track of max profit from 1 transaction up to this point
			maxThusFar = max(maxThusFar, profits[t-1][d-1] - prices[d-1])
			profits[t][d] = max(profits[t][d-1], prices[d] + maxThusFar)
	
	return profits[-1][-1]
