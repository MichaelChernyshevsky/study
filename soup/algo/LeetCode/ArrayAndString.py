# Find Pivot Index
# def pivotIndex(nums):
#     for i in range(len(nums)):
#         sumLeft = sumRight = 0
#         for j in range(0,i):
#             sumLeft += nums[j]
#         for j in range(i+1,len(nums)):
#             sumRight += nums[j]
#         if sumLeft == sumRight:
#             return i
#     return -1
#
# print(pivotIndex([1,7,3,6,5,6]))
##----------------------------------------------------------------------##
# Largest Number At Least Twice of Others
# def dominantIndex(nums):
#     highest = max(nums)
#
#     for num in nums:
#         if num!=highest and num*2 > highest:
#             return -1
#     return nums.index(highest)
#
# print(dominantIndex([3,7,6,1,0]))
##----------------------------------------------------------------------##
# Plus One
# def plusOneRecurs(digits,index):
#     digits[index] = 0
#     if index == 0:
#         digits.insert(0,1)
#     else:
#         new_index = index - 1
#         if digits[new_index] == 9:
#             plusOneRecurs(digits,new_index)
#         else:
#             digits[new_index] = digits[new_index] + 1
#     return digits
#
# def plusOne(digits):
#     if digits[-1]!=9:
#         digits[-1] = digits[-1] + 1
#         return digits
#     else:
#         return plusOneRecurs(digits,len(digits)-1)
#
# print(plusOne([9,1]))
##----------------------------------------------------------------------##
# Diagonal Traverse
# def findDiagonalOrder(mat):
#     height = len(mat)
#     weight = len(mat[0])
#     print(height,weight)
#     result = []
#     _height = 0
#     _weight = 0
#     up = True
#     while len(result) != height*weight:
#         if up == True:
#             while _height >= 0 and _weight < weight:
#                 result.append(mat[_height][_weight])
#
#                 _height -= 1
#                 _weight += 1
#             if _weight == weight:
#                 _weight -= 1
#                 _height += 2
#             else:
#                 _height += 1
#
#             up = False
#
#         else:
#             while _height < height and _weight >= 0:
#                 result.append(mat[_height][_weight])
#                 _weight -= 1
#                 _height += 1
#
#             if _height == height:
#                 _height -= 1
#                 _weight += 2
#             else:
#                 _weight += 1
#
#             up = True
#     return result
# print(findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
##----------------------------------------------------------------------##
# Spiral Matrix
# def spiralOrder(matrix):
#     row = len(matrix[0])
#     column = len(matrix)
#     _row = _column = 0
#     result = []
#     rightDirection = True
#     while len(result) != row*column:
#         if rightDirection == True:
#             while _row != row-1:
#                 if matrix[_column][_row] in result:
#                     break
#                 result.append(matrix[_column][_row])
#                 _row += 1
#             while _column != column:
#                 if matrix[_column][_row] in result:
#                     break
#                 result.append(matrix[_column][_row])
#                 _column+=1
#             _column -= 1
#             _row -= 1
#             rightDirection = False
#         else:
#             while _row != 0:
#                 if matrix[_column][_row] in result:
#                     break
#                 result.append(matrix[_column][_row])
#                 _row -= 1
#             while _column != 0:
#                 if matrix[_column][_row] in result:
#                     break
#                 result.append(matrix[_column][_row])
#                 _column-=1
#             _column += 1
#             _row += 1
#             rightDirection = True
#     return result
# print([1,2,3],"\n",[4,5,6],"\n",[7,8,9],"\n",[10,11,12])
# print(spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))
##----------------------------------------------------------------------##
# Pascal's triangle
# def generate(numRows):
#     _row = 1
#     while _row <= numRows:
#         _arr = [1]
#         if _row != 1:
#             _element = 1
#             while _element < _row:
#                 pass
#             _arr.append[1]
#         _row += 1
#         print(_arr)
#     print("finish")
# generate(2)
##----------------------------------------------------------------------##
# Add Binary
# def addBinary(a, b) -> str:
#         return '{0:b}'.format(int(a, 2) + int(b, 2))
# print(addBinary("11","1"))
##----------------------------------------------------------------------##
# Implement strStr()
# def strStr(haystack, needle):
#     if haystack is None or needle is None:
#             return -1
#     if haystack == needle:
#         return 0
#     needleLength = len(needle)
#     for i in range(len(haystack) - needleLength + 1):
#         if haystack[i:i + needleLength] == needle:
#             return i
#     return -1
# print(strStr("sadbutsad","sad"))
##----------------------------------------------------------------------##
# Longest Common Prefix
# def longestCommonPrefix(strs):
#     if len(strs) == 0:
#          return ""
#     current = strs[0]
#     for i in range(1,len(strs)):
#         temp = ""
#         if len(current) == 0:
#             break
#         for j in range(len(strs[i])):
#             if j<len(current) and current[j] == strs[i][j]:
#                temp+=current[j]
#             else:
#                break
#         current = temp
#     return current
# print(longestCommonPrefix(["school","schedule","scotland"]))
##----------------------------------------------------------------------##
#  Reverse String
# def reverseString(s):
#         i, j = 0, len(s) - 1
#         while i < j:
#             s[i], s[j] = s[j], s[i]
#             i += 1
#             j -= 1
##----------------------------------------------------------------------##
# Array Partition I
# def arrayPairSum(nums):
#         nums = sorted(nums)
#         return sum([nums[i] for i in range(0, len(nums), 2)])
##----------------------------------------------------------------------##
# Two Sum II - Input array is sorted
def twoSum(nums, target):
        start, end = 0, len(nums) - 1
        
        while start != end:
            sum = nums[start] + nums[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start + 1, end + 1]
##----------------------------------------------------------------------##


##----------------------------------------------------------------------##


##----------------------------------------------------------------------##


##----------------------------------------------------------------------##


##----------------------------------------------------------------------##


##----------------------------------------------------------------------##


##----------------------------------------------------------------------##
