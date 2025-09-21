from collections import deque

dq = deque()
dq.append(3) # appends at the e nd
dq.append(4)
dq.appendleft(2)
dq.appendleft(1)  # appends element at the beginning
print(dq)
dq.pop() # removes element at the end
dq.popleft()  # removes element at the beginning
print(dq)

dq_list = deque([1, 2, 3, 4, 5])
dq_list.rotate(1) # shifts element to the right
print(dq_list) # [5, 1, 2, 3, 4]
dq_list.rotate(-1)
print(dq_list)

dq_list.extend([6, 7, 8, 9])
print(dq_list)
dq_list.extendleft([10, 11, 12, 13])
print(dq_list)

bounded_dq = deque([1, 2, 3],maxlen=3) # bounded deque
print(bounded_dq)
bounded_dq.append(0) # if maxlen reached then removes element in the beginning and add the new element at the end
print(bounded_dq)