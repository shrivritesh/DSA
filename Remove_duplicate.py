# removes duplicate from sorted array

# def removeDup(nums):

#     slow = 0
#     fast = 1

#     while fast < len(nums):
#         if nums[slow] != nums[fast]:
#             slow += 1
#             nums[slow] = nums[fast]
#         fast += 1

#     return slow + 1


# nums = [1,1,1,2,2,3,3,4,4,5]

# k = removeDup(nums)
# print(k)
# print(nums[:k])


# Using for loop;

def removeDuplicate(nums):

    slow = 0

    for fast in range(1,len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1

num = [1,1,2,3,3,4,5,5,6,7]

k = removeDuplicate(num)

print(k)
print(removeDuplicate(num))
print(num[:k])