# compare to lists if the list contain same elemets in different indexs.
#if the element is exist print elements are same:
L1=[1,2,3,4,5,6]
L2=[6,5,4,3,2,1,7,8,9]
L3 = []
L4 = []

# for i in L2:
#     # print(i)
#     if i not in L1:
#         L3.append(i)
# print(L3)

L1 = [1, 2, 3, 4, 5, 6, 10, 11]
L2 = [6, 5, 4, 3, 2, 1, 7, 8, 9]

# Check elements in L1 that are not in L2
print("Elements in L1 but not in L2:")
for i in range(len(L1)):
    found = False
    for j in range(len(L2)):
        if L1[i] == L2[j]:
            found = True
            break
    if not found:
        print(L1[i])

# Check elements in L2 that are not in L1
print("\nElements in L2 but not in L1:")
for i in range(len(L2)):
    found = False
    for j in range(len(L1)):
        if L2[i] == L1[j]:
            found = True
            break
    if not found:
        print(L2[i])


nums = ['a', 0, 0, 1, 1, 5, 1, 2, 2, 5, 3, 3, 4, 'b', 'a']

unique_nums = []

for i in range(len(nums)):
    duplicate = False
    for j in range(len(unique_nums)):
        if nums[i] == unique_nums[j]:
            print(unique_nums[j],'#')
            duplicate = True
            break
    if not duplicate:
        unique_nums.append(nums[i])

print("List after removing duplicates:")
print(unique_nums)


# List after removing duplicates:
# output::['a', 0, 1, 5, 2, 3, 4, 'b']
# nums = ['a', 0, 0, 1, 1, 5, 1, 2, 2, 5, 3, 3, 4, 'b', 'a']
#
# unique_nums = []
# for item in nums:
#     if item not in unique_nums:
#         unique_nums.append(item)
#
# print("List after removing duplicates:")
# print(unique_nums)









