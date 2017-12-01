# Traveling Salesman Problem - Visualizer
## Description

The Traveling Salesman Problem (TSP), is one of the most intesively studied problems in computing and optimization. Given a list of cities, and the distances between then, what is the shortest path that visits each city exactly once, and return to the first city.

It belongs to the class of NP-complete problems, meaning that the worst-case running time for the solutions increases superpolynomially with the number of cities. So, any case which contains more than 20 or so cities, becomes unfeasible. 

So, we built a visualizer for the TSP, where, a random graph with 4 or 5 nodes is generated, and then, a step-by-step visualization of the problem being solved, is shown.The algorithms used to solve the problem are:

* Brute Force - O(n!): Where each permutation is tested, storing the path if it's optimal related to the past ones.
* Nearest Neighbor - O(n²): For each node, checks all it's neighbors that have not been visited yet, and finds the one with the least distance. Adds to the past. It's non-optimal, basing itself in heuristics.

## Requirements
* [Python3](https://www.python.org/download/releases/3.0/)
* [NetworkX](https://github.com/networkx/networkx)
* [Matplotlib](https://github.com/matplotlib/matplotlib)

## Installation
1. Install required packages, described on [Requirements](#requirementes). If you have pip installed, you can just run 'pip install -r requirements.txt'.
2. Run 'main.py', using the command 'python3 main.py'. If you have any error, you can look if there's as solve on [Troubleshooting](#troubleshooting).

## Troubleshooting
* [No module named tkinter](https://stackoverflow.com/questions/36327134/matplotlib-error-no-module-named-tkinter)
