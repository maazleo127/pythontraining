# # # import queue

# # # # Create a FIFO queue
# # # fifo_queue = queue.Queue()

# # # # Add elements to the queue
# # # fifo_queue.put(1)
# # # fifo_queue.put(2)
# # # fifo_queue.put(3)

# # # # Retrieve elements from the queue
# # # print(fifo_queue.get())  # prints 1
# # # print(fifo_queue.get())  # prints 2
# # # print(fifo_queue.get())  # prints 3
# # from collections import deque

# # # Create a FIFO queue using deque
# # fifo_queue = deque()

# # # Add elements to the queue
# # fifo_queue.append(1)
# # fifo_queue.append(2)
# # fifo_queue.append(3)
# # fifo_queue.append(4)

# # # Retrieve elements from the queue
# # print(fifo_queue.popleft())  # prints 1
# # print(fifo_queue.popleft())  # prints 2
# # print(fifo_queue.popleft())  # prints 3
# # print(fifo_queue.popleft())
# from collections import deque

# # create an empty deque
# fifo_queue = deque()

# # add elements to the back of the queue
# fifo_queue.append(1)
# fifo_queue.append(2)
# fifo_queue.append(3)

# # remove elements from the front of the queue
# first_item = fifo_queue.popleft()
# second_item = fifo_queue.popleft()

# print(first_item)   # Output: 1
# print(second_item)  # Output: 2
# print(fifo_queue)   # Output: deque([3])
