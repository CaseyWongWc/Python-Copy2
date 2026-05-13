challenge activity
14.6.1: Enter the output of recursive exploration.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output
```python

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
```
146
164
416
461
614
641

1
2
Check
Next
Correct The code recursively generates and outputs all combinations of nums_to_reorder values: 1, 4, and 6.

For each value in nums_to_reorder:
The first output is the current value, followed by the remaining two values of nums_to_reorder in order.
Ex: If the current value is 1, the output is 146.
The second output is the current value, followed by the remaining two values of nums_to_reorder, but in reverse order.
Ex: If the current value is 1, the output is 164.
Thus, the output is:
146
164
416
461
614
641
Yours	146
164
416
461
614
641
Expected	
146
164
416
461
614
641
