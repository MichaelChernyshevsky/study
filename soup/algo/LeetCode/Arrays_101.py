# Max Consecutive Ones
# def findMaxConsecutiveOnes(nums):
#         maxCounter = 0
#         _counter = 0
#         for i in range (len(nums)):
#             if nums[i] == 1:
#                 _counter +=1
#                 if maxCounter < _counter:
#                     maxCounter = _counter
#             else:
#                 if maxCounter < _counter:
#                     maxCounter = _counter
#                 _counter = 0
#         return maxCounter
# print(findMaxConsecutiveOnes([1,0,1,1,0,1]))
##----------------------------------------------------------------------##
# Find Numbers with Even Number of Digits
# def findNumbers(nums):
#         _counter = 0
#         for i in range( len(nums)):
#             numberToString = str(nums[i])
#             for j in range(len(numberToString)):
#                 if int(numberToString[j])%2 == 0:
#                     if  j == len(numberToString)-1:
#                         _counter +=1
#                     continue
#                 else:
#                     break
#         return _counter
# print(findNumbers([555,901,482,1771]))
##----------------------------------------------------------------------##
# Squares of a Sorted Array
# def sortedSquares(nums):
#     for i in range(len(nums)):
#         nums[i] = nums[i]**2
#     nums.sort()
#     return nums
#
# print(sortedSquares([-7,-3,2,3,11]))
##----------------------------------------------------------------------##
# Duplicate Zeros
# def duplicateZeros(arr):
#     maxLen = len(arr)
#     index = 0
#     while index != maxLen:
#         print(arr[index])
#         if arr[index] == 0:
#             arr.insert(index,0)
#             print(arr[index])
#             index+=2
#         else:
#             index+=1
# duplicateZeros([1,0,2,3,0,4,5,0])
##----------------------------------------------------------------------##
# Merge Sorted Array
# def merge(nums1, m, nums2, n):
#     _result = []
#     nums1.sort()
#     nums2.sort()
#     while len(nums1) != 0 or len(nums2)!= 0:
#         if  (len(nums1) == 0 and len(nums2)!= 0):
#             _result.append(nums2.pop(0))
#         elif  (len(nums2) == 0 and len(nums1)!= 0) :
#             _result.append(nums1.pop(0))
#         elif (nums1[0] <= nums2[0]):
#             _result.append(nums1.pop(0))
#         elif   (nums1[0] > nums2[0]) :
#             _result.append(nums2.pop(0))
#     return  _result
# print(merge([1,2,3,0,0,0],3,[2,5,6],3))
##----------------------------------------------------------------------##
# Remove Element
# def removeElement(nums, val):
#     _index = 0
#     while nums[_index]!= "_":
#         print(nums)
#         if nums[_index] == val:
#             nums.pop(_index)
#             nums.append("_")
#         else:
#             _index+=1
#     return nums
#
#
# print(removeElement([0,1,2,2,3,0,4,2],2))
##----------------------------------------------------------------------##
# Remove Duplicates from Sorted Array
# def removeDuplicates(nums):
#     _index = 1
#     while nums[_index]!="_":
#         if nums[_index] == nums[_index-1]:
#             nums.pop(_index)
#             nums.append('_')
#         else:
#             _index+=1
#     return nums
# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
##----------------------------------------------------------------------##
# Check If N and Its Double Exist
# def checkIfExist(arr):
#     for i in range(len(arr)//2 +1):
#         if i <= 0:
#             for j in range(len(arr)):
#                 if j < len(arr) and arr[j]*2 == arr[i]:
#                     return True
#         elif i < len(arr):
#             for j in range(len(arr)):
#                 if j <= 0 and arr[i]*2 == arr[j]:
#                     return True
#     return False
# print(checkIfExist([3,1,7,11]))
##----------------------------------------------------------------------##
# Valid Mountain Array
# def validMountainArray(arr):
#     checker = True
#     _up = True
#     _down = False
#     index = 1
#     while checker == True and index!=len(arr):
#         if arr[index-1] < arr[index]:
#             if _up == False:
#                 return  False
#         elif arr[index-1] > arr[index]:
#             _up = False
#             _down = True
#         elif arr[index-1] == arr[index]:
#             return False
#         index += 1
#     if _up == False and _down == True:
#         return True
#     else:
#         return  False
#
# print(validMountainArray([10,1,2,3,5,3,2,1]))
##----------------------------------------------------------------------##
# Replace Elements with Greatest Element on Right Side
# def replaceElements(arr):
#     index = 0
#     while index<=len(arr)-1:
#         if index == len(arr)-1:
#             arr[index] = -1
#         else:
#             arr[index] = max(arr[index+1:len(arr)])
#         index += 1
#     return arr
# print(replaceElements([17,18,5,4,6,1]))
##----------------------------------------------------------------------##
# Remove Duplicates from Sorted Array
# def removeDuplicates(nums):
#     index = 1
#     while nums[index] != '_':
#         if nums[index-1] == nums[index]:
#             nums.remove(index)
#             nums.append('_')
#         else:
#             index += 1
#     return  nums
#
# print(removeDuplicates([1,1,1,1,2,2,3,4,5]))
##----------------------------------------------------------------------##
# Move Zeroes
# def moveZeroes(nums):
#     index = 0
#     while index <= len(nums)-1:
#         if nums[index] == 0:
#             nums.append(nums.pop(index))
#         index += 1
#     return nums
#
# print(moveZeroes([0,1,0,3,12]))
##----------------------------------------------------------------------##
# Sort Array By Parity
# def sortArrayByParity(nums):
#     index = 0
#     maximum = len(nums)-1
#     while index!=maximum:
#         if nums[index]%2 == 1:
#             _index = index +1
#
#             while _index != maximum:
#                 if nums[_index]%2 ==1 :
#                     _index +=1
#                 else:
#                     _index = False
#                     break
#             if _index==False:
#                 nums.append(nums.pop(index))
#         index += 1
#     return nums
#
# print(sortArrayByParity([1,2,3,4,5]))
##----------------------------------------------------------------------##
# Height Checker
# def heightChecker(heights):
#     before = []
#     for i in range(len(heights)):
#         before.append(heights[i])
#     heights.sort()
#     counter = 0
#     for i in range(len(heights)):
#         if before[i] != heights[i]:
#             counter += 1
#     return counter
# print(heightChecker([7,1,2,3,4,5]))
##----------------------------------------------------------------------##
# Third Maximum Number
# def thirdMax(nums):
#     nums.sort(reverse=True)
#     if len(nums) > 2:
#         maximum = nums[0]
#         counter = 1
#         for i in range(1,len(nums)):
#             if nums[i] < maximum:
#                 counter +=1
#                 if counter == 3 :
#                     return nums[i]
#                 maximum = nums[i]
#     else:
#         return nums[0]
# print(thirdMax([1,2,4,3,23,4,5,6,2]))
##----------------------------------------------------------------------##
# Find All Numbers Disappeared in an Array
# def findDisappearedNumbers(nums):
#     nums.sort()
#     n = [ i for i in range(1,len(nums)+1)]
#     array = []
#     print(nums,n)
#     for i in range (len(nums)):
#         if nums[i] != n[i]:
#             array.append(n[i])
#     return array
# print(findDisappearedNumbers([1,1,3,3,5,5,6,6,7,8]))
##----------------------------------------------------------------------##
# Squares of a Sorted Array
# def sortedSquares(nums):
#         for i in range(len(nums)):
#             nums[i] = nums[i]**2
#         nums.sort()
#         return nums
# print(sortedSquares([-7,1,2,3,4,0,5,6,-3]))
##----------------------------------------------------------------------##
