# -*- coding: utf-8 -*-
"""Sudoku Solver

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/176ZCG5M9zqXnoJe2BQz4mEuORbnR6SLr
"""

# Sudoku solver 

# A 2-D array having 9 rows and 9 columns to take the input of the sudoku to be solved
# board is defined as a list
board = [
    [0,0,0,2,6,0,7,0,1], 
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0],
]

# a function defined whether the elements entered in each row and column is valid or not 
def valid_rowandcolumn(board, row, col): #the function is defined 
  s1 = set()
   #a set is used to store the elements that are read until now and elements keep on adding if the entered blank is not zero
  s2 = set() 
   # this set serves the same purpose for elements column-wise

  for i in range(0,9):
    if(board[row][i]) in s1:
       #checks if the element is repeated 
      return False

    if(board[row][i] != 0):
      #elements gets added to set if the element is not zero
      s1.add(board[row][i])

  for j in range(0,9):
    #the same purpose is served for the elements column-wise
    if(board[i][col]) in s2:
      return False

    if(board[i][col] != 0):
      #elements gets added to set 2 here
      s2.add(board[i][col])

  return True
  #finally returns true if all the conditions are proved true

def valid_3x3(board, row_start, col_start):
  #Here, the elements are checked for repetition in a 3 X 3 Box 
   #the entire 9 x 9 matrix is split into 9 (3 x 3) boxes for easier computation
  s1 = set()
  #s1 is a set storing the elements read until then

  for i in range(0,3):
    #takes 0,1 or 2 into account among the 9 (3x3) boxes
    for j in range(0,3):
      valid = board[i + row_start][j + col_start]

      if valid in s1:
        return False

      if(valid != 0):
        #elements gets added to set if the element read is not equal to zero
        s1.add(board[i + row_start][j + col_start])

    return True
    #finally returns true if all the conditions are proved right


def valid_sudoku(board, row, col):
  return(valid_rowandcolumn(board, row, col) and valid_3x3(board, row - row % 3, col - col % 3))
   #return type gives a value 0 or 1 based on whether the entered functions are proved true or not 
    #row - row % 3 is used to harness all the elements in the 3x3 box that is splitted 
 
     

def valid_sudoku_with_all_conditions_checked(board, element):
  #board denotes the input sudoku
   #number denotes the no. of rows and columns which are basically assumed to be equal in this case being a square

  for a in range(0,9,1):
    for b in range(0,9,1):

      if(valid_sudoku(board, a, b)):
        #checks the valid condition for each element in the row and column
        return True
    
    return False




# The main function that solves sudoku and returns the output
def solve(board):
  find = returnrow_column(board) 
  #calling the function and returns the position of elements filled as zero in the form of row,col
  if not find:
    return True
  else:
    row,col = find
     #stores the position


  for i in range(1,10):
    #the entered range of numbers should be from 1 to 9
    if valid(board, i, (row,col)):
      #board is the input
      #i is the number to be entered
      #(row,col) denotes the position in which i is stored
      board[row][col] = i

      if solve(board):
        #checks whether the sudoku is solved or not
        return True

      board[row][col] = 0
      #else part

  return False
  #if the sudoku is not solvable 

def valid(board, num, pos):
  # a function to check the validity of the entered number and where backtracking is performed 
   
   for i in range(len(board[0])):
     #board[0] denote the entire row
     if (board[pos[0]][i] == num and pos[1] != i):
       #pos[0][1] = i,j which is stored from the returnrow_column()
       return False


   for j in range(len(board[0])):
     if(board[j][pos[1]] == num and pos[0] != i):
       return False


   box_x = pos[1] // 3 
   # returns the value as either 0,1 or 2
   box_y = pos[0] // 3
   #returns the value as 0,1 or 2

   for i in range(box_y*3, box_y*3 + 3):
     #the value is permuted between 0,1 and 2
     for j in range(box_x*3,box_x*3 + 3):
       if(board[i][j] == num and (i,j) != pos):
         #stores the value of the number if its valid and not repeating in the present row and column
         return False


   return True
   #else returns true


def printsudoku(board): # a function defined to print the input sudoku in the form of a table
  # i is used for harnessing each element row-wise
  for i in range(len(board[0])): 
    if(i % 1 == 0 and i != 0):
      print("-------------------------------------------")
      #used to differentiate each row

    #j is used for harnessing each element column_wise
    for j in range(len(board[0])):
      #this condition is used so that there are no limits printed at the starting and ending column
      if(j != 0): 
        print("|", end = " ")
        #used to differentaite each column

      if( j==8 ):
        #elements are taken in the form of string
        print(str(board[i][j])) 
      else:
        #end = " " is used so that all the elements are printed row wise and then goes to the subsequent column
        print(str(board[i][j]) + " " ,end = " ") 

#a function to return the empty blanks
def returnrow_column(board):
  for i in range(len(board[0])):
    for j in range(len(board[0])):
      if(board[i][j] == 0):
        #output will be in the format of row, column
        return(i,j) 
  
  return None 
  #if there are no empty blanks the function returns sudoku as it is

print("A demo version of the Sudoku is taken into consideration here!")
print("The sudoku is solved using the method of back tracking")
print("Enter 0 if you want to run the code using the demo sudoku or enter 1 to enter the values yourself")
a = int(input("Please enter your choice:"))

if(a == 1):
  print("A valid sudoku contains elements ranging from 0 to 9, enter cautiously!!")
  #enter the elements in each seperate block and not in the same block
  bd = []
  #a list which temporarily storers the elements which are entered
  for i in range(9):
    r = []
    #a final list which are used to append the elements row-wise and aggregate all the elements entered in bd[]
    for j in range(9):
      r.append(int(input()))
    bd.append(r)

  for i in range(0,9):
    for j in range(0,9):
      #this loop is used to print the elements in the form of a horizontal tab to check where you went wrong in case invalid error is explained 
      print(bd[i][j],end = " ")



  if (valid_sudoku_with_all_conditions_checked(bd,9)):
    #takes the sudoku as input and calls the functions to solve the sudoku 
   print("Valid Sudoku")

   #Invoking the main functions to print the final value
   print("\nThe Input Sudoku looks like this:")
   printsudoku(bd)
   solve(bd) #calling the function to solve sudoku
   print("\n")

   print("The Solved Version of Your Entered Sudoku looks like this:")
   printsudoku(bd)
   #the sudoku is solved and printed in the form of the table 

  else:
    print("Invalid Sudoku! This is impossible to solve")
    print("Please enter the right values in the right blanks again")


#the conditions in the case if the user enters zero
else:
  if (valid_sudoku_with_all_conditions_checked(board,9)):
   print("Valid Sudoku")

   #Invoking the main functions to print the final value
   print("\nThe Input Sudoku looks like this:")
   printsudoku(board)
   solve(board) #calling the function to solve sudoku
   print("\n")

   print("The Solved Version of Your Entered Sudoku looks like this:")
   printsudoku(board)


  # an else part of the inner if condition
  else:
    print("Invalid Sudoku! This is impossible to solve")
    print("Please enter the right values in the right blanks again")



