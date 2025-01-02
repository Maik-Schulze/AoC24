#define a function to calculate whether a report is safe (levels are all either increasing or decreasing by 1-3)
def is_safe_report(report):

    #check if all adjacent elements are increasing by 1, 2, or 3
    increasing = all(
        report[i + 1] > report[i] and 1 <= report[i + 1] - report[i] <= 3
        for i in range(len(report) - 1)
    )
    
    #check if all adjacent elements are decreasing by 1, 2, or 3
    decreasing = all(
        report[i + 1] < report[i] and 1 <= report[i] - report[i + 1] <= 3
        for i in range(len(report) - 1)
    )
    
    #return True if one or both variables are True, else return False
    return increasing or decreasing

#define file path containing input data
file_path = "inputs/input2.txt"

#read file content, split it into integers and store tupels in a list
with open(file_path, "r") as file:
    rows = [tuple(map(int, line.split())) for line in file if line.strip()]

#call the funtion and print the result
safe_reports = [row for row in rows if is_safe_report(row)]
print(len(safe_reports))