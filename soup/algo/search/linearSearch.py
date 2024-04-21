def LinearSearch(nums,element):
    for num in nums:
        if num == element:
            return nums.index(num)
    return -1
print(LinearSearch([1,2,3,4,5],5))
