#import re for regular expression operations
import re

#define a function to calculate the sum of all valid mul instructions in a given file
def calculate_mul_sum(input_file_path):

    #regular expression to match valid mul(x,y) instructions
    pattern = r"mul\((\d+),(\d+)\)"

    #initialize variable for total sum
    total_sum = 0

    #read file content
    with open(input_file_path, "r") as file:
        content = file.read()
    
    #find all matches of the pattern in the file content
    matches = re.findall(pattern, content)

    #process all matches and calculate sum
    for x,y in matches:
            total_sum += int(x) * int(y)

    return total_sum

#define file path containing input data
file_path = "inputs/input3.txt"

#call the funtion and print the result
result = calculate_mul_sum(file_path)
print(f"The sum of all valid mul instructions is: {result}")