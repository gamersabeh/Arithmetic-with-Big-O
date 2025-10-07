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

# Iterative Fibonacci
def fibonacci(n):
    a, b = 0, 1
    if n <= 0:
        print("incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2, n):
            a, b = b, a + b
        return b
# Time Complexity: O(n)

# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 0:
        return "incorrect input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
# Time Complexity: O(2^n)

def main():
    logged_in = False
    username = "admin"
    password = "1234"

    while True:
        print("\nPlease login and choose an option:")
        print("1. Factorial of a number")
        print("2. Find the maximum number in a list")
        print("3. Linear search for a target in a list")
        print("4. Fibonacci of a number")
        print("5. Login")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "5":  # Login
            user = input("Enter username: ")
            pwd = input("Enter password: ")
            if user == username and pwd == password:
                logged_in = True
                print(" Login successful!")
            else:
                print(" Login failed! Incorrect username or password.")
        # Time Complexity: O(1)

        elif choice == "6":  # Exit
            print(" Program ended")
            break
        # Time Complexity: O(1)
        
        elif not logged_in:
            print(" You must log in first!")
        # Time Complexity: O(1)

        elif choice == "1":  # Factorial
            n = int(input("Enter a number: "))
            print(f"Factorial of ", n, "is", factorial(n))
        # Time Complexity: O(n)
        
       
