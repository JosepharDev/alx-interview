# :book: 0x01. Lockboxes
## Topics Covered
1. Python.
2. Lockboxes.
## Concepts Needed:
### Lists and List Manipulation:
  - Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
[Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)
### Graph Theory Basics:
  - Although not explicitly required, knowledge of graph theory (especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful in solving this problem, as the boxes and keys can be thought of as nodes and edges in a graph.
[Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)
### Algorithmic Complexity:
  - Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms.
[Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/)
### Recursion:
  - Some solutions might require a recursive approach to traverse through the boxes and keys.
[Recursion in Python (Real Python)](https://realpython.com/python-recursion/)
### Queue and Stack:
  - Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes.
[Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)
### Set Operations:
  - Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
[Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)
## Additional Resources
- [Mock Technical Interview](https://www.youtube.com/watch?feature=shared&v=V8DGdPkBBxg)

# :computer: Tasks.
## [0. Lockboxes](0-lockboxes.py)
### Task requirements.
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

  *  Prototype: def canUnlockAll(boxes)
  *  boxes is a list of lists
  *  You can assume all keys will be positive integers
      *  There can be keys that do not have boxes
  *  The first box boxes[0] is unlocked
  *  Return True if all boxes can be opened, else return False
```
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
```

```
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```

### :wrench: Task setup.
```bash
# Create task file and set write permission.
touch ./0-lockboxes.py
chmod +x ./0-lockboxes.py
./0-lockboxes.py

# Lint the code.
pycodestyle ./0-lockboxes.py
pep8 ./0-lockboxes.py

# Create test file
touch ./0-main.py
chmod +x ./0-main.py
./0-main.py
```

### :heavy_check_mark: Solution.
> [:point_right:  Open 0-lockboxes.py](0-lockboxes.py)
