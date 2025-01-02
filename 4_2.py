#define a function to calculate the pattern occurrences in a given file
def find_xmas_patterns(input_file_path):
    #read file content as a grid
    with open(input_file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    #define variables for amount of rows and columns as well as a counter for the pattern
    rows, cols = len(grid), len(grid[0])
    pattern_count = 0

    #check for "X-MAS" patterns with the current cell as the center
    for y in range(1, rows - 1):  #valid range for diagonals, as center cannot be on first or last row
        for x in range(1, cols - 1):  #valid range for diagonals, as center cannot be on first or last column
            if grid[y][x] == 'A':  #center must be 'A'

                #check diagonals for "MAS" patterns
                diagonals = [
                    [grid[y - 1][x - 1], grid[y][x], grid[y + 1][x + 1]],  # Top-left to bottom-right
                    [grid[y - 1][x + 1], grid[y][x], grid[y + 1][x - 1]],  # Top-right to bottom-left
                ]
                if(''.join(diagonals[0]) in {'MAS', 'SAM'} and ''.join(diagonals[1]) in {'MAS', 'SAM'}):
                    pattern_count += 1
    return pattern_count

#define file path containing input data
file_path = 'inputs/input4.txt'

#call the funtion and print the result
result = find_xmas_patterns(file_path)
print(f"The amount of occurrences of the target \"X-MAS\" pattern is: {result}")