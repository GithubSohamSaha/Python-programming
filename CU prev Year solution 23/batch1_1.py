def expanding(numlist):
    # Check if the list has at least two elements
    if len(numlist) < 2:
        return False
    
    # Check if the absolute difference between each adjacent pair strictly decreases
    for i in range(1, len(numlist) - 1):
        if abs(numlist[i] - numlist[i-1]) <= abs(numlist[i+1] - numlist[i]):
            return False
    return True

# Driver program to test the function
def test_expanding():
    test_cases = [
        ([2, 3, 5, 9, 15, 24], False),
        ([2, 3, 4, 6], False),
        ([2, 10, 16, 20], True)
    ]

    for nums, expected_result in test_cases:
        result = expanding(nums)
        print(f"List: {nums}, Result: {result}, Expected: {expected_result}")
        assert result == expected_result, f"Test failed for {nums}"

test_expanding()
