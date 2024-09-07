nums1: list = [57, 68, 78, 88, 96, 98, 1401]
nums2: list = [0, 32, 64, 88, 128, 128, 256, 512]

n = len(nums2)  # nums2 elements length
m = len(nums1)  # nums1 elements length
[nums1.append(0) for z in range(n)]

n1p_last = m + n - 1
n1p = m - 1

while nums2:
    last = nums2.pop()
    if last == 32:
        pass
    if last > nums1[n1p]:
        nums1[n1p_last] = last

    elif last == nums1[n1p]:
        nums1[n1p_last] = last
        nums1[n1p_last-1] = last
        n1p_last -= 1
        n1p -= 1

    else:
        nums1[n1p_last] = nums1[n1p]
        nums2.append(last)
        n1p -= 1

    n1p_last -= 1

    if n1p < 0:
        for num in nums2[::-1]:
            nums1[n1p_last] = num
            n1p_last -= 1
        break

if nums1 == sorted(nums1):
    print(True)
    print(nums1)

# x = eval("2.5+4*(8+2)-abs(2-10)") # string form of python code
# print(x)

# eval("print('Hello Sajjad')") # string form of python code
print('0-1Ab'.lower())