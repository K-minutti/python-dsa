
def get_max_profit(h: list, l: list, s: list):
    max_profit = 0
    for i in range(len(s)):
        b_day =  s[i]
        for j in range(i,len(s)):
            p = s[j] - b_day
            if (p> max_profit):
                max_profit = p
    return max_profit

# The solution above is O(n^2)
# we have two for loops and perform some 
# constant time operations


if __name__ == "__main__":
    h = []
    l = []
    s = [1.34, 1.50, 1.55, 1.2, 1.23, 1.5, 1.6, 1.28]
    r = get_max_profit(h, l, s)
    print(1.6 - 1.2)
    print(r)
    


