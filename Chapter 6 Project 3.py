def isSorted(lst):
    # A list is sorted if it's empty or has a single element
    if len(lst) <= 1:
        return True
    
    # Loop through each pair of elements
    for i in range(len(lst) - 1):
        # Check if the current element is greater than the next
        if lst[i] > lst[i + 1]:
            return False
    return True

# Tester program
if __name__ == "__main__":
    # Test cases
    print("Testing isSorted function:")
    
    test_cases = [
        ([], True),
        ([1], True),
        ([1, 2, 3, 4, 5], True),
        ([5, 4, 3, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([1, 2, 2, 3, 4], True)
    ]
    
    for lst, expected in test_cases:
        result = isSorted(lst)
        print(f"isSorted({lst}) = {result}, expected {expected}")
