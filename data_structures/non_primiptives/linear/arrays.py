import array 

print(array.typecodes)
heights = array.array('d', [66.7, 60.2, 72.0, 69.5, 73.1])
print(heights)


print(heights[0])

heights.insert(0, 70.25)
print(heights)
heights.remove(70.25)
print(heights)
print(heights.index(72.0))
heights.update(0, 66.5)