# Unit Test Execution Report for Calculator and Utility Functions

## Test Results Summary

### Calculator Class Tests

1. **Test Case for `add` Method**
   - Input: (2, 3)
   - Expected Output: 5
   - Status: Passed

2. **Test Case for `add` Method**
   - Input: (5, -3)
   - Expected Output: 2
   - Status: Passed

3. **Test Case for `add` Method**
   - Input: (-2, -3)
   - Expected Output: -5
   - Status: Passed

4. **Test Case for `subtract` Method**
   - Input: (5, 3)
   - Expected Output: 2
   - Status: Passed

5. **Test Case for `subtract` Method**
   - Input: (3, 5)
   - Expected Output: -2
   - Status: Passed

6. **Test Case for `subtract` Method**
   - Input: (-5, -3)
   - Expected Output: -2
   - Status: Passed

7. **Test Case for `multiply` Method**
   - Input: (3, 4)
   - Expected Output: 12
   - Status: Passed

8. **Test Case for `multiply` Method**
   - Input: (2, -3)
   - Expected Output: -6
   - Status: Passed

9. **Test Case for `multiply` Method**
   - Input: (0, 5)
   - Expected Output: 0
   - Status: Passed

10. **Test Case for `divide` Method**
    - Input: (10, 2)
    - Expected Output: 5.0
    - Status: Passed

11. **Test Case for `divide` Method**
    - Input: (10, -2)
    - Expected Output: -5.0
    - Status: Passed

12. **Test Case for `divide` Method**
    - Input: (10, 0)
    - Expected Output: Raises ValueError("Cannot divide by zero")
    - Status: Passed (Error expected)

### `reverse_string` Function Tests

1. **Test Case for `reverse_string`**
   - Input: "hello"
   - Expected Output: "olleh"
   - Status: Passed

2. **Test Case for `reverse_string`**
   - Input: ""
   - Expected Output: ""
   - Status: Passed

3. **Test Case for `reverse_string`**
   - Input: "abc!@#"
   - Expected Output: "#@!cba"
   - Status: Passed

### `is_palindrome` Function Tests

1. **Test Case for `is_palindrome`**
   - Input: "racecar"
   - Expected Output: True
   - Status: Passed

2. **Test Case for `is_palindrome`**
   - Input: "hello"
   - Expected Output: False
   - Status: Passed

3. **Test Case for `is_palindrome`**
   - Input: "A man a plan a canal Panama"
   - Expected Output: False
   - Status: Passed (without normalization)

4. **Test Case for `is_palindrome`**
   - Input: "A Santa at NASA"
   - Expected Output: False
   - Status: Passed (without normalization)

5. **Test Case for `is_palindrome`**
   - Input: ""
   - Expected Output: True
   - Status: Passed