import random
import heapq

cardinality = 10
buffer = [random.randint(1, cardinality ** 2) for i in range(cardinality)]
buffer_as_list = buffer[:]
heapq.heapify(buffer)
print(buffer, buffer_as_list)
new = random.randint(1, cardinality ** 2)
print(new)
heapq.heappush(buffer, new)
print(buffer)
while buffer:
    print(heapq.heappop(buffer))
