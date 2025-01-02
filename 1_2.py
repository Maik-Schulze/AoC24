#import Counter to count numbers
from collections import Counter

#define a function to calculate the similarity score
def calculate_similarity_score(input_file_path):

    #read file content, split it into integers and store tupels in a list
    with open(input_file_path, "r") as file:
        rows = [tuple(map(int, line.split())) for line in file if line.strip()]

    #extract both columns of numbers from the list of tuples
    column1 = [row[0] for row in rows]
    column2 = [row[1] for row in rows]

    #calculate the amount of number appearences in the second column
    right_counts = Counter(column2)

    #calculate and return similaity score (sum of multiplication of every entry in the left column with appearence count of the same number in right column)
    return(sum(number * right_counts[number] for number in column1))

#define file path containing input data
file_path = "inputs/input.txt"

#call the funtion and print the result
similarity_score = calculate_similarity_score(file_path)
print(f"The similarity score is: {similarity_score}")