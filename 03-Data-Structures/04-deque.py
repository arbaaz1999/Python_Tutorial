"""Deque in Python"""

from collections import deque

de = deque()  # initializing an empty deque
print("Initialized empty deque : ", de)
de.append(10)  # appends 10 to the end // [10]
print("After appending 10 : ", de)
de.append(20)  # // [10, 20]
print("After appending 20 : ", de)
de.append(30)  # // [10, 20, 30]
print("After appending 30 : ", de)
de.appendleft(5)  # [5, 10, 20, 30]
print("After appending 5 to the left : ", de)

de.extend([8, 10])  # extends the deque from the end // [5, 10, 20, 30, 8, 10]
print("After extending [8, 10] : ", de)

de.extendleft(
    [0, 2, 3]
)  # extend the deque to the left side // [0, 2, 3, 5, 10, 20, 30, 8, 10]
print("After extending [0, 2, 3] to the left : ", de)

last = de.pop()  # remove and return the element from the last
print(f"{last} has been removed from the end of the deque")

first = de.popleft()  # remove and return the element from the first
print(f"{first} has been removed from the first of the deque")

de.remove(
    20
)  # removes the first occurance of given element, raise ValueError if not present
print("After removing 20 from the deque : ", de)

de.rotate(3)  # rotate the deque by 3 position to the right
print("After Rotating 3 position to the right : ", de)

de.rotate(-4)  # rotate the deque by 4 position to the left
print("After rotating 4 position to the left : ", de)

count = de.count(8)  # counts the number of occurance of given element
print(f"Number 8 appears {count} times")

index = de.index(
    10
)  # return the index of given element, raise ValueError if not present
print(f"Element 10 appear at {index} position")

de.insert(3, 8)  # will insert the element 8 at 3rd index
print("After adding 8 at 3rd index : ", de)

de.reverse()  # reverse the deque
print("After reversing the deque : ", de)

de.clear()  # removes all element from the deque
print("Deque Cleared : ", de)
