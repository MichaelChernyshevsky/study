def SelectionSort(nums):
    for i in range(0,len(nums)-1):
        minIndex = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[i],nums[minIndex] = nums[minIndex],nums[i]
    return nums

print(SelectionSort([5,4,3,2,1]))
