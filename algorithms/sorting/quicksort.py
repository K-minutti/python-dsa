def sort(arr: list) -> None:
    quicksort(arr, 0, len(arr)-1)
    
def quicksort(arr: list, low: int, hi: int) -> None:
    """If there are items to sort...
    sorted_pivot is the final index of the pivot 
    that was used in the sort step (sort in respect to the pivot)
    """
    if low < hi: 
        sorted_pivot = sort_partition(arr, low, hi)
        quicksort(arr, low, sorted_pivot-1) 
        quicksort(arr, sorted_pivot+1, hi)


def sort_partition(arr: list, low: int, hi: int) -> int: 
    """Notice there is a two-pointer approach to sorting the 
    elements less than the pivot the left and the items greater 
    than the pivot to the right with a slow pointer and a fast pointer.
    """
    partition = low # slow pointer 
    pivot = arr[hi]   # Could use hueristic of finding avg of low, mid, hi instead we are just using hi
    for fast_ptr in range(low, hi):
        if arr[fast_ptr] <= pivot:
            arr[partition], arr[fast_ptr] = arr[fast_ptr], arr[partition]
            partition +=1
    # place pivot in it's final place now that items to left are less than
    # pivot and items to the right are greater than pivot
    arr[partition], arr[hi] = arr[hi], arr[partition]
    return partition

    
def iterative_quicksort(arr: list):
    pass