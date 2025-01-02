#define a function to calculate the distance of two lists of numbers given in a single file
def find_list_distance(input_file_path):

    #read file content, split it into integers and store tupels in a list
    with open(input_file_path, "r") as file:
        rows = [tuple(map(int, line.split())) for line in file if line.strip()]

    #extract and sort both columns of numbers from the list of tuples
    column1 = sorted(row[0] for row in rows)
    column2 = sorted(row[1] for row in rows)

    #calculate the total distance as the sum of absolute differences between corresponding elements
    sum_distance = sum(abs(a - b) for a, b in zip(column1, column2))

    return sum_distance

#define file path containing input data
file_path = "inputs/input.txt"

#call the funtion and print the result
distance = find_list_distance(file_path)
print(f"The total distance is: {distance}")