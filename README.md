# Tower Of Hanoi

1. Introduction
Game Setting:
- Tower of Hanoi is a game with usually 3 pegs and a fixed number of disks.
- For this project, we have used 4 pegs and the number of discs (n) keep increasing
up to a runtime of 10 minutes
- The initial state is defined by all the disks in the leftmost peg, i.e. Peg1 with the
largest disk at the bottom and the smallest on the top.
- The goal state is where all disks are moved over to the rightmost peg, i.e. Peg4 with
the largest disk at the bottom and the smallest on the top.

Game Rule:
- Possible to move only one disk per move to any other peg.
- Only the top most disk on a peg can be moved to other pegs, i.e. the larger sized
disc has to always be below the smaller sized disk.

There were two kinds of search algorithms implemented for this puzzle game:
- A* Search algorithm
- Breadth first search
A* search algorithm is a smart and a flexible algorithm that can be used to solve large
range of problems in the best and the shortest path (cost in our case). It gives a more
realistic result as it considers the current state and considers how far the current state
from the goal state is in order to draw the best possible path. 
