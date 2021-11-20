# Step 1
sudo = [[2, 8, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]
        
for i in sudo:
        print(i)

# Step 2
size = 9
def find_number(row, col, num):
    # check if number exists in row, if it does return false and check the next number form 1-9 until one doesnt
    for x in range(9):  
        if sudo[row][x] == num:
            return False
    # check if number exists in coloumn, if it does return false and check the next number form 1-9 until one doesnt         
    for x in range(9):
        if sudo[x][col] == num:
            return False
 
    # check if number exists in the 3x3 subgrid , if it does return false and check the next number form 1-9 until one doesnt
    startRow = row - row % 3 
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudo[i + startRow][j + startCol] == num:
                return False
    return True

# Step 3
def iterate_through( row, col):
    
    #once all numbers allocated it reaches the end of sudoku return true 
    if (row == size - 1 and col == size):
        return True

    #go to the next row if end of column reached
    if col == size:
        row += 1
        col = 0
    #if box has number already alocated run this same function on the next column (col+1) 
    if sudo[row][col] > 0:
        return iterate_through( row, col + 1)

    #if box is empty or unlocated go through numbers 1-9 and check whcih number is to be allocated
    for num in range(1, size + 1): 
     
        if find_number( row, col, num):
            sudo[row][col] = num
            
            if iterate_through( row, col + 1):
                return True
        sudo[row][col] = 0
    return False      

# Step 4
print('\n')
if iterate_through( 0, 0)==True:
    for i in sudo:
        print(i)
else:
    print("No solution found!")