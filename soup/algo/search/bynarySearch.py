def BinarySearch(nums,element):
    size = len(nums)-1
    lowIndex  = 0
    highIndex = size
    midInedex = (lowIndex+highIndex)//2
    midElement = nums[midInedex]

    while True:
        print(nums[lowIndex:highIndex])
        if lowIndex == highIndex:
            return -1
        elif midElement == element:
            return midInedex
        elif midElement > element:
            highIndex = midInedex + 1
            midInedex = (lowIndex+highIndex)//2
            midElement = nums[midInedex]
        elif midElement < element:
            lowIndex = midInedex + 1
            midInedex = (lowIndex+highIndex)//2
            midElement = nums[midInedex]
    return - 1

print(BinarySearch([1,2,3,4,5,6,7],4))
