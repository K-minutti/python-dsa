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
