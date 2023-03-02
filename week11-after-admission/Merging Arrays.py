lengths = input()

nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
merged = []

ptr1 = 0
ptr2 = 0

while ptr1 < len(nums1) and ptr2 < len(nums2):
    if nums1[ptr1] < nums2[ptr2]:
        merged.append(nums1[ptr1])
        ptr1 += 1
    else:
        merged.append(nums2[ptr2])
        ptr2 += 1
        
while ptr1 < len(nums1):
    merged.append(nums1[ptr1])
    ptr1 += 1
    
while ptr2 < len(nums2):
    merged.append(nums2[ptr2])
    ptr2 += 1
    
print(*merged)

#5min
#1sub