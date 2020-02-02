
def insertion_sort(nums):

    for i in range(1, len(nums)):
        for j in range(i-1, 0, -1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                # tmp = nums[j]
                # nums[j] = nums[j+1]
                # nums[j+1] = tmp
            else:
                break
        print(nums)
    return nums
nums = [5,4,6,1,3]
insertion_sort(nums)