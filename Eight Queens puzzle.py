# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 20:15:33 2019

@author: rabia
"""
import random

my_list = []
size=8


def general(size):
    
    solving()

def solving():
        """Solve the n queens puzzle and print the number of solutions"""
        position = [-1] *size
        queen(position, 0)
        

def queen(position, row):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the function calls itself trying to place a queen
        on the next row until all N queens are placed on the NxN board.
        """
        solutions = 0

        # Base (stop) case - all N rows are occupied
        if row == size:
            fullboard(position)
            # self.show_short_board(positions)
            solutions += 1
        else:
            # For all N columns positions try to place a queen
            for column in range(size):
                # Reject all invalid positions
                if checking(position, row, column):
                    position[row] = column
                    queen(position, row + 1)


def checking(positions, fullrow, column):
        """
        Check if a given position is under attack from any of
        the previously placed queens (check column and diagonal positions)
        """
        for i in range(fullrow):
            if positions[i] == column or \
                positions[i] - i == column - fullrow or \
                positions[i] + i == column + fullrow:

                return False
        return True

def fullboard(positions):
        """Show the full NxN board"""
        for row in range(size):
            line = ""
            for column in range(size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")


def main():
    """Initialize and solve the n queens puzzle"""
    general(8)
    my_list.append(general(8))
if __name__ == "__main__":
    # execute only if run as a script
    main()

a = random.randint(0,len(my_list))

print (my_list[a])



