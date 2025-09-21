from collections import Counter

numbers = ["a", 'b', 'c', 'a', 'd', 'b', 'a', 'd', 'f']

counter = Counter(numbers)
counter.update(['x', 'x'])
counter.update('yy') # considered as two strings y: 2 , better to pass it an array like above line
print(counter)

counter.update(a=7) # updates the counter value
print(counter)

counter.subtract(a=6)
print(counter)

print(counter.most_common())
print(counter.most_common(1)) # first record

counter.clear()
print(counter)