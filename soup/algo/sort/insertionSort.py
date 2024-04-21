def InsertionSort(nums):
    for i in range(1,len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and temp < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = temp
    return nums

print(InsertionSort([5,4,3,2,1]))
