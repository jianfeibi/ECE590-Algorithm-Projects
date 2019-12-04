"""
Math 590
Project 3
Fall 2019

Partner 1: Jianfei Bi (jb577)
Partner 2: Xichen Tan (xt124)
Date: 2019-11-12
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage

This function implements Bellman-Ford algorithm, to detect and report a 
negative cost cycle in the currency graph.

This function takes in a graph and the tolerance value, and outputs a 
single list of vertex ranks corresponding to the negative cost cycle. 
"""


def detectArbitrage(currencies, tol=1e-15):

    # Set initial dist and previous vertex.
    # currencies.adjList represents 'graph' in the pseudo code.
    # for vertex in currencies.adjList:
    #     vertex.dist = math.inf
    #     vertex.prev = None

    # Set the distance from the starting vertex to 0.
    # The first vertex in the currencies list is the starting vertex.
    currencies.adjList[0].dist = 0

    # Iterate over the whole list, |V| - 1 times in total.
    for iter in range(0, len(currencies.adjList) - 1):
        # Look at each vertex.
        for u in currencies.adjList:
            # Check each neighbour of u.
            # Update predictions and previous vertex.
            for i in u.neigh:
                # Only update if the new value is better.
                # We cannot trust any updates of a size smaller than the tolerance value.
                if i.dist > u.dist + currencies.adjMat[u.rank][i.rank] + tol:
                    i.dist = u.dist + currencies.adjMat[u.rank][i.rank]
                    i.prev = u

    # Run for 1 extra iteration to detect any potential negative cost cycles.
    # If any updates appeared in this iteration, there exists NCC in the graph.
    # Set a boolean variable to keep track of whether NCC exists.
    ncc_record = None
    update = False
    for u in currencies.adjList:
        for i in u.neigh:
            if i.dist > u.dist + currencies.adjMat[u.rank][i.rank] + tol:
                ncc_record = u
                update = True
                break

    # If this iteration breaks before it goes through all the vertices,
    # the vertex update_record is the starting vertex of the
    # negative cost cycles.
    # Set a list ncc to keep track of vertices in NCC.
    ncc = []
    if update is True:
        # The NCC cycle starts with ncc_record.
        ncc.append(ncc_record.rank)
        u = ncc_record.prev
        while u.isEqual(ncc_record) is False:
            ncc.append(u.rank)
            u = u.prev
        # The NCC cycle ends with ncc_record.
        ncc.append(ncc_record.rank)

    # Since we traced the path backwards, we need to reverse the path.
    ncc.reverse()

    return ncc

################################################################################

"""
rates2mat

This function creates the adjacency matrix with the 
correctly weighted edges. 

"""


def rates2mat(rates):
    return [[ -math.log(R) for R in row] for row in rates]


"""
Main function.
"""
if __name__ == "__main__":
    testRates()

