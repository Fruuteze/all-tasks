def bub(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(bub([2, 7, 3, 5]))

def qiq(arf, left, right):
    if len(arf) < 2:
        return arf
    mi = arf[0]
    left_arf = []
    right_arf = []
    for i in range(left, right):
        if mi > arf[i]:
            left_arf.append(arf[i])
        elif mi != arf[i]:
            right_arf.append(arf[i])

    res_left = qiq(left_arf, 0, len(left_arf))
    res_right = qiq(right_arf, 0, len(right_arf))
    res_left.append(mi)
    res_left.extend(res_right)
    return res_left


print(qiq([3, 7, 2, 9], 0, 4))
