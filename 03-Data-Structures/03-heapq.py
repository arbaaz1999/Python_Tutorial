import heapq

"""Heap queue or heapq in Python"""

""" 1. Creating a Heap Queue """

li = [20, 15, 10, 30, 40]  # Creating a list

heapq.heapify(li)  # Convert the list into a heap

print("Heap Queue : ", li)


""" 2. Appending and Popping Elements from a Heap Queue """

heapq.heappush(
    li, 5
)  # heappush() is used to append the element while maintaining the order of the heap

min = heapq.heappop(li)

print(li)
print("Smallest element is : ", min)
print(li)


""" 3. Appending and Popping Simultaneously """

min = heapq.heappushpop(li, 2)

print("Smallet element added and removed in one go : ", min)
print(li)


""" 4. Finding the Largest and Smallest Elements in a Heap Queue """

h = [5, 10, 15, 20, 25, 30]
heapq.heapify(h)

n_largest = heapq.nlargest(3, h)
n_smallest = heapq.nsmallest(3, h)

print("3rd Largest Element is : ", n_largest[-1])
print("3rd smallet element is : ", n_smallest[-1])


""" 5. Replace and Merge Operations on Heapq """

min = heapq.heapreplace(
    h, 23
)  # it replaced the minimum element with the  given element
print(f"{min} is replaced with 23. {h}")

h2 = [24, 22, 21, 25]
# heapq.heapify(h2)

h3 = list(heapq.merge(h, h2))
print("After merging ", h3)
