def BubbleSort(nums):
    for i in range(0,len(nums)-1):
        for j in range(0,len(nums)-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1],nums[j]
    return nums

print(BubbleSort([4,1,5,2,5,7,9,10,1,2,3,1]))
