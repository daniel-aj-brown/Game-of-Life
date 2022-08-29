# Game-of-Life

An implmentation of John Conway's Game of Life.

A 2D array represents a collection of celula automata which live and die when certain conditions are met:

- If an alive cell is surrounded by exactly 2 or 3 living neighbours, they continue to survive.
- If a dead cell is surrounded by exactly 3 living neighbours, it comes to life as if by a migrating population.
- Otherwise the cell dies, as if by over population in the case of 4 or more neighbours or by underpopulation in the case of zero or 1 living neighbour.

The game plays automatically without requring inpurt from the user. Interesting paterns and immergent properties can be observed as populations rise and fall over time, as if battling over resources. They can migrate around the map and even stablize in they own areas until invaded by other cells.

The user decides the number of cells and size of each cell in pixels before running the program.
