a = "abcabc"

max = 0
chh = ''
count = [0] * 256
for ch in a : count[ord(ch)] += 1
for ch in a :
    if(count[ord(ch)] > max):
        max = count[ord(ch)]
        chh = ch
print(a[::3])
print(chh)


def findSingle(ar, n):
    res = ar[0]

    # Do XOR of all elements and return
    for i in range(1, n):
        res = res ^ ar[i]

    return res


# Driver code
ar = [5, 3, 5, 4, 5, 3, 4]
print("Element occurring once is", findSingle(ar, len(ar)))
