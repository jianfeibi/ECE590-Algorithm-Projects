"""
Math 590
Project 4
Fall 2019

Partner 1: Xichen Tan
Partner 2: Jianfei Bi
Date: 12/5/2019
"""

# Import math, itertools, and time.
import math
import itertools
import time

# import numpy
import numpy as np

# Import the Priority Queue.
from p4priorityQueue import *

################################################################################

"""
Prim's Algorithm
"""
def prim(adjList, adjMat):
    ##### Your implementation goes here. #####
    # Class Vertex already helps us initialize all costs to inf and prev to null
    # Pick an arbitrary start vertex and set cost to 0
    index = np.random.randint(0,len(adjList))
    start = adjList[index]
    start.cost = 0

    # Make the priority queue using cost for sorting
    PQ = PriorityQueue(adjList)

    while not PQ.isEmpty():
        # Get the next unvisited vertex and visit it
        v = PQ.deleteMin()
        v.visited = True

        # For each edge in v.neigh:
        for neighbor in v.neigh:
            # If the edge leads out, update
            if not neighbor.visited:
                if neighbor.cost > adjMat[v.rank][neighbor.rank]:
                    neighbor.cost = adjMat[v.rank][neighbor.rank]
                    neighbor.prev = v
    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):
    ##### Your implementation goes here. #####
    # Initialize all singleton sets for each vertex
    for vertex in adjList:
        makeset(vertex)

    # Initialize the empty MST
    X = []

    # Sort the edges by weight
    edgeList.sort()

    # Loop through the edges in increasing order
    for edge in edgeList:
        # If the min edge crosses a cur, add it to our MST
        u, v = edge.vertices
        if find(u) != find(v):
            X.append(edge)
            union(u, v)
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    ##### Your implementation goes here. #####
    v.pi = v
    v.height = 0
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.
"""
def find(v):
    ##### Your implementation goes here. #####
    while v != v.pi:
        v = v.pi
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    ##### Your implementation goes here. #####
    # First, find the root of the tree for u
    # and the tree for v
    ru = find(u)
    rv = find(v)

    # If the sets are already the same, return
    if ru == rv:
        return

    # Make shorter set point to taller set
    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
    else:
        # Same height, break tie
        ru.pi = rv

        # Tree got taller, increment rv.height
        rv.height += 1
    return

################################################################################

"""
TSP
"""
def tsp(adjList, start):
    ##### Your implementation goes here. #####
    tour = []
    stack = []
    # implement DFS first
    # initialize all vertices as unvisited first
    for vertex in adjList:
        vertex.visited = False
    start.visited = True

    # push the start vertex onto array
    stack.append(start)

    while len(stack):
        # get the current city
        current = stack.pop()
        tour.append(current.rank)

        # push all unvisited neighbors onto the stack
        # visit them and record where we came from
        for neighbor in current.mstN:
            if neighbor.visited is False:
                stack.append(neighbor)
                neighbor.visited = True
    # append the start.rank
    tour.append(start.rank)
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p4tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
