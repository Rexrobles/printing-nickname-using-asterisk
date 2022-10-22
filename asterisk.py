# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)

# REFERENCE 

# print(" ****   *****   *   * ") 
# print(" *   *  *        * *  ")
# print(" ****   *****     *   ")
# print(" *  *   *        * *  ")
# print(" *  *   *****   *   * ")

displayName = "REX"
print_R = [[" " for int_col in range(5)] for int_row in  range(5)]
print_E = [[" " for int_col in range(5)] for int_row in  range(5)]
print_X = [[" " for int_col in range(5)] for int_row in  range(5)]

#code for R
for row in range(5):
    for col in range(5):
        if col == 0 or (col == 4 and (row != 0 and row !=2)) or (row==0 or row==2 and (col>0 and col< 4)):
            print_R[row][col] = "*"

#code for E
for row in range(5):
    for col in range(5):
        if (col == 0 or (row == 0 or row == 2 or row == 4) and (col > 0)):
            print_E[row][col] = "*"

#code for X
for row in range(5):
    for col in range(5):
        if (row+col==4) or  (row-col==0):
            print_X[row][col] = "*"

for int_col in range (5):
    for int_row in range(5):
        print(print_R[int_col][int_row], end = "")
    print(end = "  ")
    for int_row in range(5):
        print(print_E[int_col][int_row], end = "")
    print(end = "  ")
    for int_row in range(5):
        print(print_X[int_col][int_row], end = "")
    print()