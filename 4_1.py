#directions for searching: (dy, dx)
#dy: row movement, dx: column movement
directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1),   # Right
    (-1, -1), # Up-Left
    (-1, 1),  # Up-Right
    (1, -1),  # Down-Left
    (1, 1)    # Down-Right
]

#define the target word and its length
target_word = "XMAS"
word_length = len(target_word)

#define a helper function to check for target word starting at (y, x) in a given direction
def check_occurrence(y, x, dy, dx, grid, target_word):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i in range(word_length):
        ny, nx = y + i * dy, x + i * dx
        if not (0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == target_word[i]):
            return 0
    return 1

#define a function to calculate the target word occurrences in a given file
def find_word_occurrences(input_file_path):

    #read file content as grid
    with open(input_file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    
    #count total occurrences of target word in all directions
    total_count = 0
    rows, cols = len(grid), len(grid[0])
    for y in range(rows):
        for x in range(cols):
            for dy, dx in directions:
                total_count += check_occurrence(y, x, dy, dx, grid, target_word)
    
    return total_count

#define file path containing input data
file_path = 'inputs/input4.txt'

#call the funtion and print the result
result = find_word_occurrences(file_path)
print(f"The amount of occurrences of the target word \"{target_word}\" is: {result}")