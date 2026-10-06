"""print duplicates"""
s = "programming"

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in freq:
    if freq[ch] > 1:
        print(ch)
"""frequency of a string"""
s = "programming"

dup = {}

for i in s:
    if i in dup:
        dup[i] += 1
    else:
        dup[i] = 1
print(dup)

s = "programming"

dup = {}

for i in s:
    if i in dup:
        dup[i] += 1
    else:
        dup[i] = 1

for i in dup:
    print(i, "->", dup[i])

"""first non duplicate in a string"""
s = "aabbccdef"

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
"""anagram using dict"""
s1 = "race"
s2 = "races"
s11 = {}
if len(s1) != len(s2):
    print("not anagram")
else:
    for i in s1:
        if i in s11:
            s11[i] += 1
        else:
            s11[i] = 1
    for i in s2:
        if i in s11:
            s11[i] -= 1
        else:
            s11[i] = -1
    c = 0
    for i in s11.values():
        if i != 0:
            c = 1
            break
    if c == 0:
        print("Anagaram")
    else:
        print("Not Anagaram")
"""duplicate char"""
s = "banana"
dup = {}

for i in s:
    if i in dup:
        dup[i] += 1
    else:
        dup[i] = 1

for i in dup:
    if dup[i] > 1:
        print(i)
"""first repeated"""
s = "abcdefca"
seen = {}
for i in s:
    if i in seen:
        print(i)
        break
    else:
        seen[i] = 1

"""selection sort"""
arr = [6, 3, 8, 2, 7]

for i in range(len(arr)):
    min_index = i

    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)

"""finding a elments that sum =target using two pointers"""
a = [1, 2, 4, 6, 8, 9]
target = 10

left = 0
right = len(a) - 1

while left < right:
    total = a[left] + a[right]

    if total == target:
        print("found")
        print(a[left], a[right])
        break

    elif total > target:
        right -= 1

    # elif total < target:
    else:
        left += 1
"""palindrome using pointers """
s = "madam"

left = 0
right = len(s) - 1

while left < right:

    if s[left] != s[right]:
        print("Not Palindrome")
        break

    left += 1
    right -= 1

else:
    print("Palindrome")
a = [2, 5, 8, 12, 16, 20]
target = 16
s=0
end=len(a)-1
while s<=end:
    mid=(s+end)//2
    if a[mid]==target:
        print("Found")
        break
    elif a[mid]>target:
        end=mid-1
    else:
        s=mid+1
else:
    print("not found")