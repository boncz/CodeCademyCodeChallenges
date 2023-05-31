#Find the Xth Number In Order
#Write a function, getX, that given an integer x and a list nums 
#returns the Xth number if the list was in sorted order. 
#In other words, the Xth smallest number.

def getX(x, nums):
  nums.sort()
  if x > 0 and x <= len(nums):
    return nums[x-1]
  else:
    return 0

