
def reorder_nums(remain_nums, reordered_nums):
    if len(remain_nums) == 0:
        print(reordered_nums[0], reordered_nums[1], reordered_nums[2], sep='')
    else:
        for i in range(len(remain_nums)):
            tmp_remain_nums = remain_nums[:] # Make a copy.
            tmp_removed_num = tmp_remain_nums[i] 
            tmp_remain_nums.pop(i) # Remove element at i
            reordered_nums.append(tmp_removed_num)
            reorder_nums(tmp_remain_nums, reordered_nums)
            reordered_nums.pop() # Remove last element

nums_to_reorder = []
result_nums = []

nums_to_reorder.append(1)
nums_to_reorder.append(4)
nums_to_reorder.append(6)

reorder_nums(nums_to_reorder, result_nums)