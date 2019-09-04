# README

## What is this repository for

* Advanced Algorithms and Data Structures class
* Class notes
* Code templates
* Solutions

## How do I get set up

**Note**: Windows users may have to use `py -3` instead of `python3` and **\\** instead of **/**.

* Clone the repository.

```bash
git clone git@github.com:LutherCS/aads-class-pub.git
```

* Get updates.

```bash
git pull origin master
```

* Create and activate Python 3.7 virtual environment

```bash
sudo apt-get install python3.7-venv
python3.7 -m venv .venv
source .venv/bin/activate
```

* Specify **PYTHONPATH** in *.env*

```bash
PYTHONPATH=.
```

Note that *.env* is excluded from version control by default and has to be added to each copy of the repository

* Install *pythonds3* to use textbook implementations of various data structures and algorithms.

```bash
python3 -m pip install -U pythonds3
```

* Install linters *pylint*, *flake8*, and *mypy*.

```bash
python3 -m pip install -U pylint mypy flake8 flake8-mypy
```

* Install formatter *black*.

```bash
python3 -m pip install -U black
```

* Install testing framework *pytest* and *pytest-timeout* plugin.

```bash
python3 -m pip install -U pytest pytest-timeout
```

* Install *colorama* that is used to highlight output.

```bash
python3 -m pip install -U colorama
```

* Run a project

```bash
python3 src/projects/module/file.py
```

* Test a project.

```bash
python3 -m pytest tests/projects/module/test_file.py
```

* Check code coverage

```bash
python3 -m pytest --cov tests/
```

* Generate the presentation

```bash
pandoc -s -i --slide-level=2 -t revealjs topic.md -o topic.html
```

* Prepare the assignment

**Note**: module name (*hello*), file name (*hello_main*), and function name (*greet_by_name*) don't have to match.

* Edit *src/exercises/hello/description.md*.
* Edit *src/exercises/hello/hello_main.py*.
* Edit *tests/exercises/hello/test_hello.py*.

## Topics

* Python review
  * Tools: black, pylint, pytest
  * Collection data types
  * Exceptions and errors
  * Magic methods
  * Descriptors
  * Data classes
  * Modern Python features

* Algorithm analysis
  * [Master theorem](https://xlinux.nist.gov/dads/HTML/mastertheorm.html)
  * [asymptotic time complexity](https://xlinux.nist.gov/dads/HTML/asymptoticTimeComplexity.html)

* Basic data structures
  * [stack](https://xlinux.nist.gov/dads/HTML/stack.html)
  * [queue](https://xlinux.nist.gov/dads/HTML/queue.html)
  * [deque](https://xlinux.nist.gov/dads/HTML/deque.html)
  * [linked list](https://xlinux.nist.gov/dads/HTML/linkedList.html)
  * [doubly linked list](https://xlinux.nist.gov/dads/HTML/doublyLinkedList.html)

* Recursion
  * [recursion](https://xlinux.nist.gov/dads/HTML/recursion.html)

* Searching
  * [linear search](https://xlinux.nist.gov/dads/HTML/linearSearch.html)
  * [binary search](https://xlinux.nist.gov/dads/HTML/binarySearch.html)
  * [dictionary](https://xlinux.nist.gov/dads/HTML/dictionary.html)
  * [set](https://xlinux.nist.gov/dads/HTML/set.html)
  * [Judy array - Wikipedia](https://en.wikipedia.org/wiki/Judy_array)
  * [Bloom filter](https://xlinux.nist.gov/dads/HTML/bloomFilter.html)
  * [skip list](https://xlinux.nist.gov/dads/HTML/skiplist.html)

* Sorting
  * Suboptimal algorithms
  * Optimal comparison-based algorithms

* Tree
  * [tree](https://xlinux.nist.gov/dads/HTML/tree.html)
  * [Finger tree - Wikipedia](https://en.wikipedia.org/wiki/Finger_tree)
  * [R-tree](https://xlinux.nist.gov/dads/HTML/rtree.html)
  * [Fusion tree - Wikipedia](https://en.wikipedia.org/wiki/Fusion_tree)
  * [Rose tree - Wikipedia](https://en.wikipedia.org/wiki/Rose_tree)
  * [van Emde-Boas priority queue](https://xlinux.nist.gov/dads/HTML/vanemdeboas.html)
  * [AVL tree](https://xlinux.nist.gov/dads/HTML/avltree.html)
  * [binary heap](https://xlinux.nist.gov/dads/HTML/binaryheap.html)
  * [B-tree](https://xlinux.nist.gov/dads/HTML/btree.html)
  * [B+-tree](https://xlinux.nist.gov/dads/HTML/bplustree.html)
  * [Fibonacci heap](https://xlinux.nist.gov/dads/HTML/fibonacciHeap.html)
  * [red-black tree](https://xlinux.nist.gov/dads/HTML/redblack.html)
  * [splay tree](https://xlinux.nist.gov/dads/HTML/splaytree.html)
  * [Patricia tree](https://xlinux.nist.gov/dads/HTML/patriciatree.html)
  * [trie](https://xlinux.nist.gov/dads/HTML/trie.html)
  * [leftist tree](https://xlinux.nist.gov/dads/HTML/leftisttree.html)
  * [Skew heap - Wikipedia](https://en.wikipedia.org/wiki/Skew_heap)

* Graph
  * [directed acyclic graph](https://xlinux.nist.gov/dads/HTML/directAcycGraph.html)
  * [breadth-first search](https://xlinux.nist.gov/dads/HTML/breadthfirst.html)
  * [depth-first search](https://xlinux.nist.gov/dads/HTML/depthfirst.html)
  * [best-first search](https://xlinux.nist.gov/dads/HTML/bestfirst.html)
  * [Dijkstra's algorithm](https://xlinux.nist.gov/dads/HTML/dijkstraalgo.html)
  * [Bellman-Ford algorithm](https://xlinux.nist.gov/dads/HTML/bellmanford.html)
  * [Floyd-Warshall algorithm](https://xlinux.nist.gov/dads/HTML/floydWarshall.html)
  * [minimum spanning tree](https://xlinux.nist.gov/dads/HTML/minimumSpanningTree.html)
  * [Prim-Jarnik algorithm](https://xlinux.nist.gov/dads/HTML/primJarnik.html)
  * [Kruskal's algorithm](https://xlinux.nist.gov/dads/HTML/kruskalsalgo.html)
  * [A* search algorithm - Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)

* Algorithms
  * [divide and conquer](https://xlinux.nist.gov/dads/HTML/divideAndConquer.html)
  * [greedy algorithm](https://xlinux.nist.gov/dads/HTML/greedyalgo.html)
  * [backtracking](https://xlinux.nist.gov/dads/HTML/backtrack.html)
  * [memoization](https://xlinux.nist.gov/dads/HTML/memoize.html)
  * [dynamic programming](https://xlinux.nist.gov/dads/HTML/dynamicprog.html)
  * [minimax](https://xlinux.nist.gov/dads/HTML/minimax.html)
  * [heuristic](https://xlinux.nist.gov/dads/HTML/heuristic.html)

## References

### Text Editors and IDEs

[Popular development environments](https://insights.stackoverflow.com/survey/2018) include the following:

* [Visual Studio Code](https://code.visualstudio.com/) | [setup](https://code.visualstudio.com/docs/languages/python)
* [Sublime Text](https://www.sublimetext.com/) | [setup](https://realpython.com/setting-up-sublime-text-3-for-full-stack-python-development/)
* [vim](http://www.vim.org/) | [setup](https://realpython.com/vim-and-python-a-match-made-in-heaven/)
* [Atom](https://atom.io/)
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [Jupyter Notebook](http://jupyter-notebook.readthedocs.io/en/latest/notebook.html)
* [Wing IDE](https://wingware.com/)

### Tools and Utilities

* [An Introduction to the Linux Terminal | DigitalOcean](https://www.digitalocean.com/community/tutorials/an-introduction-to-the-linux-terminal)
* [git - the simple guide - no deep shit!](http://rogerdudler.github.io/git-guide/)
* [Installing Packages — Python Packaging User Guide](https://packaging.python.org/tutorials/installing-packages/)
* [Pipenv: A Guide to the New Python Packaging Tool – Real Python](https://realpython.com/pipenv-guide/)
* [pytest: helps you write better programs — pytest documentation](https://docs.pytest.org/en/latest/)

### Python Basics

* [The Python Standard Library — Python 3.7.0 documentation](https://docs.python.org/3/library/index.html)
* [PEP 8 -- Style Guide for Python Code | Python.org](https://www.python.org/dev/peps/pep-0008/)
* [Python Style Guidelines - The Chromium Projects](https://www.chromium.org/chromium-os/python-style-guidelines)
* [mattharrison/Tiny-Python-3.6-Notebook: This repository contains the text for the Tiny Python 3.6 Notebook.](https://github.com/mattharrison/Tiny-Python-3.6-Notebook)
* [crazyguitar/pysheeet: Python Cheat Sheet](https://github.com/crazyguitar/pysheeet)

### Exception Handling

* [8. Errors and Exceptions — Python 3.6.0 documentation](https://docs.python.org/3/tutorial/errors.html)
* [Python Exceptions Handling](https://www.tutorialspoint.com/python/python_exceptions.htm)

### Object-Oriented Programming

* [Python @property: How to Use it and Why? - Programiz](https://www.programiz.com/python-programming/property)
* [Introduction to Python descriptors – IBM Developer](https://developer.ibm.com/tutorials/os-pythondescriptors/)
* [Python Tutorial: Properties vs. getters and setters](https://www.python-course.eu/python3_properties.php)
* [Descriptor HowTo Guide — Python 3.7.2 documentation](https://docs.python.org/3/howto/descriptor.html)
* [Object-Oriented Programming (OOP) in Python 3 – Real Python](https://realpython.com/python3-object-oriented-programming/)
* [Jupyter Notebook Viewer - The Tao of Python](http://nbviewer.jupyter.org/github/akittas/presentations/blob/master/pythess/tao_mro/tao_of_python.ipynb)
* [3. Data model — Python 3.7.0 documentation](https://docs.python.org/3/reference/datamodel.html)
* [Underscores in Python](https://shahriar.svbtle.com/underscores-in-python)
* [Python3 Tutorial: Magic Methods](http://www.python-course.eu/python3_magic_methods.php)
* [Python Class Examples: Init and Self - Dot Net Perls](https://www.dotnetperls.com/class-python)
* [The self variable in python explained | Python Tips](https://pythontips.com/2013/08/07/the-self-variable-in-python-explained/)
* [OOP - Inheritance](http://ccm.net/contents/422-oop-inheritance)
* [An Introduction to Classes and Inheritance (in Python) - Jessica Hamrick](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)
* [Learn Python the Hard Way - Read for Free](https://learnpythonthehardway.org/book/ex44.html)
* [Python3 Tutorial: Inheritance](http://www.python-course.eu/python3_inheritance.php)

### Algorithm Analysis

* [Analysis of Algorithms](http://www.greenteapress.com/thinkpython/html/thinkpython022.html)
* [A Gentle Introduction to Algorithm Complexity Analysis](http://discrete.gr/complexity/)
* [Analysis of Algorithms](http://aofa.cs.princeton.edu/10analysis/)

### Basic Data Structures

* [VisuAlgo - Linked List (Single, Doubly), Stack, Queue, Deque](https://visualgo.net/en/list)
* [List of data structures - Wikipedia](https://en.wikipedia.org/wiki/List_of_data_structures)

### Recursion

* [In plain English, what is recursion? - Software Engineering Stack Exchange](https://softwareengineering.stackexchange.com/questions/25052/in-plain-english-what-is-recursion)
* [An Introduction to Recursion, Part 1 – topcoder](https://www.topcoder.com/community/data-science/data-science-tutorials/an-introduction-to-recursion-part-1/)
* [An Introduction to Recursion: Part 2 – topcoder](https://www.topcoder.com/community/data-science/data-science-tutorials/an-introduction-to-recursion-part-2/)

### Searching Algorithms

* [Data Structures and Algorithms Hash Table](https://www.tutorialspoint.com/data_structures_algorithms/hash_data_structure.htm)
* [Basics of Hash Tables Tutorials & Notes | Data Structures | HackerEarth](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)

### Sorting Algorithms

* [Sorting algorithms visualized with animated color palette | FlowingData](https://flowingdata.com/2017/10/26/sorting-algorithms-visualized-with-rainbow-color-palette/)
* [Sorting Algorithm Animations | Toptal](https://www.toptal.com/developers/sorting-algorithms)
* [VisuAlgo - Sorting (Bubble, Selection, Insertion, Merge, Quick, Counting, Radix)](https://visualgo.net/bn/sorting)

### Trees

* [Binary Trees](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html)
* [Binary Trees](http://cslibrary.stanford.edu/110/BinaryTrees.html)
* [Binary Tree -- from Wolfram MathWorld](http://mathworld.wolfram.com/BinaryTree.html)

### Graphs

* [Data Structures and Algorithms Graph Data Structure](https://www.tutorialspoint.com/data_structures_algorithms/graph_data_structure.htm)
* [A Gentle Introduction to Data Structures: How Graphs Work](https://medium.freecodecamp.org/a-gentle-introduction-to-data-structures-how-graphs-work-a223d9ef8837)
* [Graph Search, Shortest Paths, and Data Structures | Coursera](https://www.coursera.org/learn/algorithms-graphs-data-structures)
