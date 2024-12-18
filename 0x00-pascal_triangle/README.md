# :book: 0x00. Pascal's Triangle
## Topics Covered
1. Python.
2. Pascal's Triangle.
## Resource
- [What is Pascal’s triangle](https://www.cuemath.com/algebra/pascals-triangle/)
- [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?v=0iMtlus-afo)
- [What are Python Algorithms](https://builtin.com/data-science/python-algorithms)
## Additional Resource
- [Mock Technical Interview](https://www.youtube.com/watch?v=1qw5ITr3k9E)
## Must Know
  To successfully complete this project, you should revise the following Python concepts:

### Lists and List Comprehensions:
  - Understand how to create, access, modify, and iterate over lists.
Utilize list comprehensions for more concise and readable code, especially for generating rows of Pascal’s Triangle.
### Functions:
  - Know how to define and call functions.
Pass parameters and return values, particularly how to return a list of lists representing Pascal’s Triangle.
### Loops:
   - Use for and while loops to iterate through sequences.
Nested loops may be necessary for generating each row and calculating the values of Pascal’s Triangle.
### Conditional Statements:
  - Apply if, elif, and else conditions to implement logic based on the position within Pascal’s Triangle (e.g., the edges of the triangle always being 1).
### Recursion (Optional):
  - While not strictly necessary, understanding recursion can provide an alternative approach to generating Pascal’s Triangle.
Recognize base cases and recursive cases for a function that generates the triangle’s rows.
### Arithmetic Operations:
  - Perform addition, a fundamental operation for calculating each element of Pascal’s Triangle as the sum of the two elements directly above it.
### Indexing and Slicing:
  - Access elements and slices of lists, crucial for identifying and summing the correct elements when constructing each row of the triangle.
### Memory Management:
  - Be mindful of how lists are stored and copied, especially when creating new rows based on the values of the previous row.
### Error and Exception Handling (Optional):
  - Use try-except blocks as needed to handle potential errors, such as invalid input types or values.
### Efficiency and Optimization:
  - Consider the time and space complexity of different approaches to generating Pascal’s Triangle.
Evaluate and apply optimizations to improve the performance of the solution.

# :computer: Tasks.
## [1. Don't make a promise...if you know you can't keep it](1-promise.js)
### Task requirements.
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

  *  Returns an empty list if n <= 0
  *  You can assume n will be always an integer
```
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 
```

### :wrench: Task setup.
```bash
# Create task file and set write permission.
touch ./0-pascal_triangle.py
chmod +x ./0-pascal_triangle.py
./0-pascal_triangle.py

pycodestyle ./0-pascal_triangle.py
pep8 ./0-pascal_triangle.py

# Create test file
touch ./0-main.py
chmod +x ./0-main.py
./0-main.py
```

### :heavy_check_mark: Solution.
> [:point_right: Go to 1-promise.js](1-promise.js)
