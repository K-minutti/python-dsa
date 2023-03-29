'''
The Boyer Moore majority voting algorithm is used to the find the majority
element in a sequence of elements.
It uses linear time and constant space.
A majority is more than (sizeof(set)/2).
https://www.cs.utexas.edu/users/moore/best-ideas/mjrty/
'''

def majority(elements: list[int]) -> int:
    """One drawback of this implementation
    is that it requires that a majority is a
    actually present in the list in order to 
    return an element that is correct.

    Args:
        elements (list[int]): 

    Returns:
        int: the majority element or the last seen element
    """
    m = None
    count = 0
    for e in elements:
        if count == 0:
            m = e
        elif e == m:
            count+=1
        else:
            count-=1
    return m


def majority_checked(elements: list[int]) -> int:
    """This implementation uses a two pass approach 
    to confirm that the element return by the first
    pass is indeed the majority

    Args:
        elements (list[int]): _description_

    Returns:
        int: _description_
    """
    majority_res = majority(elements)

    count = 0
    for e in elements:
        if e == majority_res:
            count +=1
    
    threshold = (len(elements)/2)
    if count > threshold:
        return majority_res
    else:
        return None  # there is no majority