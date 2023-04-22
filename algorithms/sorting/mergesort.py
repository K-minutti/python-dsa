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
    # https://www.geeksforgeeks.org/iterative-merge-sort/
    pass