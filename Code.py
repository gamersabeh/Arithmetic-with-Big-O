# Factorial Function
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
# Time Complexity: O(n)

# Find Max
def find_Max(nbs):
    max_val = nbs[0]
    for i in nbs:
        if i > max_val:
            max_val = i
    return max_val
# Time Complexity: O(n)

# Linear Search
def linear_search(lst, target):
    for i in lst:
        if i == target:
            return True
    return False
# Time Complexity: O(n)

