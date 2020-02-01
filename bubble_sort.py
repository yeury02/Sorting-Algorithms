
def bubbleSort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
    return nums

nums = [2,3,1,5,8,7,4,3,9,4]
print(bubbleSort(nums))