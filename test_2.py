"""
Structured English 

This program takes in grades from a text file 
It will display the number of grades
It will display the average grade
within a function that also displays the percentage of grades
that are abpve the average grade shown.
Grades above average will be done using a function calculating
the average, displaying the number of grades, and percent of grades
above the average.
"""


"""
infile = open 
grades = line in infile 
infile close
Loop number of grades 
average grades sum of grades / length 
loop grade scores 
if grade > average
print number of grades
print average grade
print percent of grades above average

main

"""

def calcuate_percent_above_average():
    infile = open("Final.txt", 'r')
    grades = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(grades)):
        grades[i] = int(grades[i])
    average = sum(grades) / len(grades)
    num = 0
    for grade in grades:
        if grade > average:
            num += 1
    print("Number of grades:", len(grades))
    print("Average grade:", average)
    print("Percent of grades above average: {0:.2f}%".format(100 * num / len(grades)))
    
    



def main():
    calcuate_percent_above_average()

main()