# Game-of-Life

An implementation of John Conway's Game of Life.
 
A 2D array represents a collection of cellular automata which live and die when certain conditions are met:
 
- If an alive cell is surrounded by exactly 2 or 3 living neighbours , they continue to survive.
- If a dead cell is surrounded by exactly 3 living neighbours , it comes to life as if by a migrating population.
- Otherwise the cell dies, as if by overpopulation in the case of 4 or more neighbours or by underpopulation in the case of too few living neighbours.
 
The game plays automatically without requiring input from the user. Interesting patterns and emergent properties can be observed as populations rise and fall over time, as if battling over resources. They can migrate around the map and even stabilise in their own areas until invaded by other migrating cells.
 
The user decides the number of cells and size of each cell in pixels before running the program.
 
Please ensure you have the Pygame and Numpy modules installed on your system before running this project.
