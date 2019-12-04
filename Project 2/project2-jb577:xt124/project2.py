"""
Math 590
Project 2
Fall 2019

project2.py

Partner 1: Jianfei Bi
Partner 2: Xichen Tan
Date: 2019-11-06
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""


def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    # #### Your implementation goes here. #####
    # ##DFS Solution
    if alg == 'DFS':
        path_rev = Stack()
        path = []
        stack = Stack()
        # No vertex visited yet, and all the visited status of vertex is already
        # set to False in initialization
        # Push the start vertex onto the stack
        stack.push(maze.start)

        while not stack.isEmpty():
            # Get the current room
            current = stack.pop()

            # Only visit if we have not visited before
            if current.visited is False:
                # Mark as visited
                current.visited = True

                # if we reach the exit of maze, then use prev
                # to track vertex back to start and store them in our path_rev
                if current.rank == maze.exit.rank:
                    while current.prev is not None:
                        path_rev.push(current.rank)
                        current = current.prev

                    # push the start vertex into path_rev
                    path_rev.push(current.rank)
                    # pass vertexes' ranks from path_rev to path
                    # then we can store start rank to exit rank from left to right
                    while not path_rev.isEmpty():
                        path.append(path_rev.pop())

                    # return our path
                    return path
                # Push all neighbors onto the stack
                # Then record its previous vertex
                for neighbor in current.neigh:
                    if neighbor.visited is False:
                        stack.push(neighbor)
                        neighbor.prev = current


    # #### Your implementation goes here. #####
    # ##BFS Solution
    if alg == 'BFS':
        path_rev = Stack()
        path = []
        queue = Queue()
        # Set all vertices to an infinite distance
        # It's already done in initialization

        # Push start vertex into the queue and set dist = 0.
        queue.push(maze.start)
        maze.start.dist = 0

        while not queue.isEmpty():
            # Get the current vertex
            current = queue.pop()

            # if we reach the exit of maze, then use prev
            # to track vertex back to start and store them in our path_rev
            if current.rank == maze.exit.rank:
                while current.prev is not None:
                    path_rev.push(current.rank)
                    current = current.prev

                # push the start vertex into path_rev
                path_rev.push(current.rank)
                # pass vertexes' ranks from path_rev to path
                # then we can store start rank to exit rank from left to right
                while not path_rev.isEmpty():
                    path.append(path_rev.pop())

                # return our path
                return path

            # Look at all of its neighbors
            for neighbor in current.neigh:
                if neighbor.dist == math.inf:
                    # Push the neighbor into the queue
                    queue.push(neighbor)

                    # Update its distance and track path
                    # Actually, we don's really care about what's the value of dist here
                    neighbor.dist = current.dist + 1
                    neighbor.prev = current

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(True)
