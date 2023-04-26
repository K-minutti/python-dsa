def sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    l = arr[:mid]
    r = arr[mid:]

    l = sort(l)    
    r = sort(r)
    return merge(l, r)

def merge(l: list, r: list) -> list:
    idx_a = 0 
    idx_b = 0
    arr = []
    while idx_a < len(l) and idx_b < len(r):
        if l[idx_a] <= r[idx_b]:
            arr.append(l[idx_a])
            idx_a +=1
        else:
            arr.append(r[idx_b])
            idx_b +=1

    arr.extend(l[idx_a:])
    arr.extend(r[idx_b:])
    return arr


def sort_selfcontained(l: list) -> list:
    if len(l) > 1: 
        mid = len(l)//2
        left = l[:mid]
        right = l[mid:]
        sort_selfcontained(left)
        sort_selfcontained(right)
        i,j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                l[k] = left[i]
                i+=1
            else:
                l[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left):
            l[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1




def sort_iterative(l: list) -> list:
    n = len(l)
    size = 1  # start with sub arrays of size 1
    
    while (size < n):
        low = 0
        while(low < n - 1):
            mid = min(low+size-1, n-1) # n-1 included for out-of bound error
            high = min(low+(size*2)-1, n-1)
            iter_merge(l, low, mid, high)
            low += size * 2
    size *= 2


def iter_merge(arr: list, low: int, mid: int, high: int):
    pass