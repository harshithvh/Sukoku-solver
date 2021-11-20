# Sukoku-solver
Python

<img align="left" alt="Visual Studio Code" width="1080px" src="https://repository-images.githubusercontent.com/356149741/2207af00-a4ef-11eb-844a-e3df4fc82eaa" />

# About

---

Sudoku is one of the most popular puzzle games of all time. As a logic puzzle, Sudoku is also an excellent brain game. Being a tech savvy you can solve this by using your python programming skills. By using basic programming concepts like functions, loops and conditions we can build a Sudoku solver program.

# Step 1: Creating a Sudoku solver

---

In this method for solving Sudoku puzzle
1. Assign the size of the 2D matrix to variable size (M*M)
2. Assign the puzzle to print the grid


# Step 2: Finding unfilled cells and assigning value

---

1. We will assign numto the row and col
2. If we find same num in the same row or same column or in the specific 3*3 matrix.
3. We match the next number

# Step 3: Validating the entries

---

1. Check if we have reached the end of the row and column
2. Verify if the sum of values in a column, row and a 3X3 grid is 9
3. If the value in the cell is greater than zero, iterate through the next column
