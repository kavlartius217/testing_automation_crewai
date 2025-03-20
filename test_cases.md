```markdown
# Unit Test Cases for Calculator and Utility Functions

## Test Cases for Calculator Class

### 1. Test Case for `add` Method
- **Description**: Test the addition of two positive numbers.
  - **Input**: (2, 3)
  - **Expected Output**: 5

### 2. Test Case for `add` Method
- **Description**: Test the addition of a positive and a negative number.
  - **Input**: (5, -3)
  - **Expected Output**: 2

### 3. Test Case for `add` Method
- **Description**: Test the addition of two negative numbers.
  - **Input**: (-2, -3)
  - **Expected Output**: -5

### 4. Test Case for `subtract` Method
- **Description**: Test the subtraction of two positive numbers.
  - **Input**: (5, 3)
  - **Expected Output**: 2

### 5. Test Case for `subtract` Method
- **Description**: Test the subtraction resulting in a negative number.
  - **Input**: (3, 5)
  - **Expected Output**: -2

### 6. Test Case for `subtract` Method
- **Description**: Test the subtraction of two negative numbers.
  - **Input**: (-5, -3)
  - **Expected Output**: -2

### 7. Test Case for `multiply` Method
- **Description**: Test the multiplication of two positive numbers.
  - **Input**: (3, 4)
  - **Expected Output**: 12

### 8. Test Case for `multiply` Method
- **Description**: Test the multiplication of a positive and a negative number.
  - **Input**: (2, -3)
  - **Expected Output**: -6

### 9. Test Case for `multiply` Method
- **Description**: Test the multiplication resulting in zero.
  - **Input**: (0, 5)
  - **Expected Output**: 0

### 10. Test Case for `divide` Method
- **Description**: Test division of two positive numbers.
  - **Input**: (10, 2)
  - **Expected Output**: 5.0

### 11. Test Case for `divide` Method
- **Description**: Test division by a negative number.
  - **Input**: (10, -2)
  - **Expected Output**: -5.0

### 12. Test Case for `divide` Method
- **Description**: Test division by zero, expecting a ValueError.
  - **Input**: (10, 0)
  - **Expected Output**: Raises ValueError("Cannot divide by zero")

## Test Cases for `reverse_string` Function

### 1. Test Case for `reverse_string`
- **Description**: Test reversing a typical string.
  - **Input**: "hello"
  - **Expected Output**: "olleh"

### 2. Test Case for `reverse_string`
- **Description**: Test reversing an empty string.
  - **Input**: ""
  - **Expected Output**: ""

### 3. Test Case for `reverse_string`
- **Description**: Test reversing a string with special characters.
  - **Input**: "abc!@#"
  - **Expected Output**: "#@!cba"

## Test Cases for `is_palindrome` Function

### 1. Test Case for `is_palindrome`
- **Description**: Test a simple palindromic string.
  - **Input**: "racecar"
  - **Expected Output**: True

### 2. Test Case for `is_palindrome`
- **Description**: Test a non-palindromic string.
  - **Input**: "hello"
  - **Expected Output**: False

### 3. Test Case for `is_palindrome`
- **Description**: Test a palindromic string with mixed case.
  - **Input**: "A man a plan a canal Panama"
  - **Expected Output**: False (without normalization)

### 4. Test Case for `is_palindrome`
- **Description**: Test a string with whitespaces and punctuation, which is a palindrome.
  - **Input**: "A Santa at NASA"
  - **Expected Output**: False (without normalization)

### 5. Test Case for `is_palindrome`
- **Description**: Test an empty string as a palindrome.
  - **Input**: ""
  - **Expected Output**: True
```