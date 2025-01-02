#import re for regular expression operations
import re

#define a function to calculate the sum of all valid mul instructions in a given file
def calculate_conditional_mul_sum(input_file_path):

    #regular expressions to match valid mul(x,y) and conditional do(), don't() instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"
    condition_pattern = r"(do\(\)|don't\(\))"

    #initialize variables
    total_sum = 0
    is_enabled = True #by default, mul instructions are enabled

    #read file content
    with open(input_file_path, "r") as file:
        content = file.read()
    
    #find all instructions in the file in order of appearance
    instructions = re.findall(f"{mul_pattern}|{condition_pattern}", content)

    #process instructions
    for instruction in instructions:
        #if a condition is matched
        if instruction[2]:
            #if matched condition is do
            if instruction[2] == "do()":
                is_enabled = True
            #if matched condition is don't
            elif instruction[2] == "don't()":
                is_enabled = False
        #if mul is matched and enabled
        elif instruction[0] and instruction[1] and is_enabled:
            x, y = int(instruction[0]), int(instruction[1])
            total_sum += x * y

    return total_sum

#define file path containing input data
file_path = "inputs/input3.txt"

#call the funtion and print the result
result = calculate_conditional_mul_sum(file_path)
print(f"The sum of all valid mul instructions considering conditions is: {result}")