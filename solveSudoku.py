#Student name: Alexander Jefferies
#ID: 592666392
#UPI:Ajef929

from math import degrees
#from SolveSodukuDefault import checkRuleOut
import copy
from typing import Iterator
import itertools
import random

class evalue:
    def __init__(self):
        self.steps = 0
        self.solved = 0
sc = evalue()
"""
A sudoku is a 9x9 matrix where each item has domain {1,2,3,4,5,6,7,8,9}. 
A sudoku problem contains a incomplete grid where some squares are missing. The missing squares are denoted by 0.
                                8 0 0 0 2 0 0 0 0 
                                0 1 0 6 5 0 8 0 3 
                                0 0 5 0 0 0 2 0 0 
                                0 0 0 2 0 0 6 0 4 
                                0 0 3 0 0 0 0 0 0 
                                2 0 7 0 0 0 5 3 0 
                                5 0 1 4 0 0 0 0 0 
                                0 0 0 0 6 2 0 1 0 
                                0 0 0 0 1 0 4 0 0 

The target is to assign a value to each missing square, such that the following rules will not be violated:
    1. any row contains all values from {1,2,3,4,5,6,7,8,9}
    2. any column contains all values from {1,2,3,4,5,6,7,8,9}
    3. The grid can be divided into 9 3x3 blocks. Each block contains all values from {1,2,3,4,5,6,7,8,9}
    an example of sudoku: 
                                8 6 4 7 2 3 1 9 5 
                                9 1 2 6 5 4 8 7 3 
                                3 7 5 8 9 1 2 4 6 
                                1 5 9 2 3 7 6 8 4 
                                6 8 3 9 4 5 7 2 1 
                                2 4 7 1 8 6 5 3 9 
                                5 2 1 4 7 9 3 6 8 
                                4 3 8 5 6 2 9 1 7 
                                7 9 6 3 1 8 4 5 2 

"""


class point:
    """
        A "point" is a square in the sudoku grid. 
        x,y denotes the horizontal-vertical position of the square.
        "available" is a list of all candidate values for this position.
        "value" is the current value for the position. The dafault is 0.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.available = []
        self.value = 0
        self.constrained = 0


def rowNum(p, sudoku):
    """
    Return  current values in p's row.
    """
    row = set(sudoku[p.y * 9:(p.y + 1) * 9])
    if 0 in row: row.remove(0)
    return row  # set type


def colNum(p, sudoku):
    """
    Return current values in p's column
    """
    col = []
    length = len(sudoku)
    for i in range(p.x, length, 9):
        col.append(sudoku[i])
    col = set(col)
    if 0 in col: col.remove(0)
    return col  # set type


def blockNum(p, sudoku):
    """
    Return current values in p's block
    """
    block_x = p.x // 3
    block_y = p.y // 3
    block = []
    start = block_y * 3 * 9 + block_x * 3
    for i in range(start, start + 3):
        block.append(sudoku[i])
    for i in range(start + 9, start + 9 + 3):
        block.append(sudoku[i])
    for i in range(start + 9 + 9, start + 9 + 9 + 3):
        block.append(sudoku[i])
    block = set(block)
    if 0 in block: block.remove(0)
    return block  # set type

def initPoint(sudoku):
    """
    Initialise the sudoku grid using the input, and return the candidate positions 
    """
    pointList = []
    length = len(sudoku)
    for i in range(length):
        if sudoku[i] == 0:
            p = point(i % 9, i // 9)
            for j in range(1, 10):
                if j not in rowNum(p, sudoku) and j not in colNum(p, sudoku) and j not in blockNum(p, sudoku):
                    p.available.append(j)
            pointList.append(p)
    return pointList
    
def ForwardCheck(pointList, sudoku):
    """
    Task 1: 
    Implement the forward checking algorithm that performs arc consistency checks
    :param pointList: a list which stores all currently unassigned variables. Each item here is a "point" entry.
    :param sudoku: current assignments. Each element denotes an assignment to the corresponding square.
    :return: an updated pointList that is the result of the arc consistency algorithm for sudoku
    """
    updatedList = []
    modifyCount = 0
    for point in pointList:
        ##equivalent AC3
        edges = set(point for point2 in pointList if (point2.x == point.x) or  (point2.y == point.y) or (point.x // 3 == point2.x // 3) and  (point.y //3 == point2.y //3))
        #edges =  samerow.union(samecol).union(sameblock)
        for edge in edges:
            navailable = []
            for val in edge.available:
                temp_edge = copy.deepcopy(edge)
                temp_edge.value = val
                if check(temp_edge,sudoku): navailable.append(val)
        checker = edge.available 
        ##how to remove all of the inferenes from assignment
        edge.available = navailable
        if checker != edge.available:
            modifyCount += 1

        updatedList.append(point)
        #print()
    ######################
    # if len(updatedList) == 0:
    #     print()

    return updatedList

def BacktrackCSP_frameWork(pointList, sudoku, select=None):
    """
    Task 2: Complete this method in the indicated code segments. 
    :param pointList: a list which stores all variables currently unassigned. Each item here is a "point" entry.
    :param sudoku: current assignments. Each element denotes an assignment to the corresponding square.
    Note: 0 denotes that this position has not been assigned.
    :return: True (if at least a solution can be find) or False(if no solution exists)
    """
    if len(pointList) <= 0:
        print("all points allocated")
        return True
    #Select the next unassigned variable
    if select == "default": #default function, just use it to support your understanding.
        pselected = select_unassigned_var(pointList, sudoku)
    elif select == "MRV":
        pselected = select_unassigned_var_MRV(pointList, sudoku)
    elif select == "New":
        pselected = select_unassigned_var_New(pointList, sudoku)
    else:
        print("select method undefined!")
        return
    flag = False
    #Implement the main framework of the backtracking algorithm:
    #Select a value from the available list of the variable "pselected" 
    #Call the ForwardCheck method to perform arc consistency check
    #Check whether assigning value to pselected will result in a conflict
    #Proceed with search or backtrack
    ######################
    potential_values = order_LCV(pselected,sudoku,pointList)
    for val in potential_values:
        pointListSave = copy.deepcopy(pointList)
        pselected.value = val
        idx = assignIdx(pselected.x,pselected.y,sudoku)
        if check(pselected,sudoku):
            sudoku[idx] = val
            ##forward checking
            infered = ForwardCheck(pointList, sudoku)
            test = len([el for el in infered if el.available == []])
            if test == 0:
                #showSudoku(sudoku)
                #if sc.steps % 100 == 0 : print("searching...",sc.steps, " steps") 
                sc.steps += 1  
                #if sc.steps % 100: showSudoku(sudoku)           
                result = BacktrackCSP_frameWork(pointList,sudoku,select=select)
                if result != False:
                    return result
    
        sudoku[idx] = 0
        pointList = pointListSave
        #showSudoku(sudoku)
        #pointList.append(pselected)        
    pointList.append(pselected)
    return flag


def testSudoku(sudoku):
    """
    Task 3: Complete this method
    :param sudoku: current assignments. Each element denotes an assignment to the corresponding square.
    :return: True (if sudoku is a valid solution), False (otherwise)
    Note: If the input is not a valid solution, print out the row, column, or block where a conflict occurs
    """
    ######################
    ### Your code here ###
    ##iterate through the 
    valid = True
    for idx, assign in enumerate(sudoku):
        ##checking to see if the current value exists in the
        test_sud = copy.deepcopy(sudoku)
        test_sud[idx] = 0
        #showSudoku(test_sud)
        test_sud_row = [item for index,item in enumerate(test_sud) if idx % 9 == index % 9 and item != 0]
        test_sud_column = [item for index,item in enumerate(test_sud) if idx // 9 == index // 9 and item != 0]
        test_sud_block = [item for index,item in enumerate(test_sud) if idx % 9 // 3 == index % 9 // 3 and idx // 9 // 3 == index // 9 // 3 and item != 0 ]
        out_str = "Invalid sudoku: value " + str(assign) + " "
        if assign in test_sud_row:
            valid = False
            ##conflict occurs
            print(out_str + "conflict in row " + str(idx % 9 + 1) +" at Position ",str(idx),"of sudoku")
            
        elif assign in test_sud_column:
            valid = False

            print(out_str +"conflict in column " + str(idx // 9 +1)+" at Position ",str(idx),"of sudoku")
            
        elif assign in test_sud_block:
            valid = False
            print(out_str +"conflict in block {0}".format((idx % 9 // 3 +1,idx // 9 // 3 + 1))+" at Position ",str(idx),"of sudoku")
        
    return valid

    
    ######################


def select_unassigned_var(pointList, sudoku):
    """
    Given a partial assignment for the sudoku puzzle, choose the next unassigned variable, 
    return it and update the "pointList".
    Note: this is the default function for selecting the next unassigned variable.
    """
    return pointList.pop()


def select_unassigned_var_MRV(pointList, sudoku):
    """
    Task 4: 
    Given partial assignment sudoku, choose the next unassigned variable, 
    return it and update "pointList".
    For this task, you need to implement the MRV heuristic for selecting the next unassigned variable.
    :param pointList: a list which stores all variables currently unassigned. Each item here is a "point" entry.
    :param sudoku: current assignments. Each element denotes an assignment to the corresponding square.
    most constrained variable
    """
    ######################
    ##make a copy of the list of points
    tmp_points = copy.deepcopy(pointList)
    inferences = ForwardCheck(tmp_points,sudoku)##removing the most unconstrained 
    checkdict = dict()
    #creating a sorted dictionary that sorts based on how many possible moves a point has
    for p in inferences:
        checkdict[p] = len(p.available)
    sorted_dict = sorted(checkdict.items(),key = lambda x: x[1],reverse=True)
    ##if there is a tiebreak
    min_val = sorted_dict[-1][1]

    ##checking to see if in need of a tie break 
    tiebreakvals = [p[0] for p in sorted_dict if p[1] == min_val]
    if len(tiebreakvals) == 1:
        el = sorted_dict[-1][0]
    ##choose out of the tie broken elements based on an outdegree heuristic
    elif len(tiebreakvals) > 1:
        point_dict = dict()
        for p in tiebreakvals:
            ##calculates the degree of the Element
            degree = 9 - len(colNum(p,sudoku)) + 9 - len(rowNum(p,sudoku)) + 9 - len(blockNum(p,sudoku))
            point_dict[p] = degree
        sorted_dict2 = sorted(point_dict.items(),key = lambda x: x[1],reverse=False)
        el = sorted_dict2[-1][0]
    
    #point_idx = [(point1,idx) for idx,point1 in enumerate(pointList) if point1.x == el.x and point1.y == el.y][0][1]
    output = [p for p in pointList if p.x == el.x and p.y == el.y][0]
    return pointList.pop(pointList.index(output))

    
        
    #orderByNumberof Possible Assignments


    
##let this heuristic be the degree heuristic returning the p with the largest number of edges 
# def degree_heuristic(tiebreakvals,pointList,sudoku):
#     edge_dict = dict()
#     for tie_point in tiebreakvals:
#         edges = set(point for point in pointList  if (tie_point.x == point.x) or  (tie_point.y == point.y) or (point.x // 3 == tie_point.x // 3) and  (point.y //3 == tie_point.y //3) and (point.x != tie_point.x and point.y != tie_point.y ))
#         edge_dict[tie_point] = len(edges)
#     sorted_dict = sorted(edge_dict.items(),key = lambda x: x[1],reverse=True)
#     min_value = sorted_dict[0][1]
#     ##tie break within this
#     tiebreakvals = [p[0] for p in sorted_dict if p[1] == min_value]
#     if len(tiebreakvals) == 1:
#         el = sorted_dict[0][0]
#     elif len(tiebreakvals) > 1:
#         ##if there is tiebreak within this then randomly choose the next element
#         el = random.choice(tiebreakvals)
#     return el

def select_unassigned_var_New(pointList, sudoku):
    """
    Task 5:
    Given a partial assignment, choose the next unassigned variable, 
    return it and update "pointList".
    For this task you need to implement a different heuristic for selecting the next unassigned variable.     
    """
    ######################
    ##this heuristic incoprorates randomness with a split chance of using the degree heuristic to imporve on the default selection of MRV heurisitc 
    rand_num = random.random()
    if rand_num <= 0.1:
        ##if the selected heuristic is only the degree heuristic or if the random integer
        point_dict = dict()
        max_degree = 0 
        for p in pointList:
            degree = 9 - len(colNum(p,sudoku)) + 9 - len(rowNum(p,sudoku)) + 9 - len(blockNum(p,sudoku))
            point_dict[p] = degree
            if degree > max_degree:
                max_degree = degree
            
        eligible_ps = [p for p in pointList if point_dict[p] == max_degree]

        if len(eligible_ps) > 1:
            ##select the rightmost point
            p = random.choice(eligible_ps)
        else:
            p = eligible_ps[0]
        selected_p = pointList.pop(pointList.index(p))
        #showSudoku(sudoku)
    else:
        #selected_p = pointList.pop()
        selected_p = select_unassigned_var_MRV(pointList,sudoku)
    #point_idx2 = [pointList.index(point) for point in pointList if point.x == el[0] and point.y == el[1]][0]
    return selected_p
    ######################
    

def assignIdx(xpos,ypos,sudoku):
        for num in range(0,len(sudoku)):
            ##check to see how thse are lined up
            t1 = num // 9
            t2 = num % 9 
            if t1 == ypos and t2 == xpos:
                idx = num
                break
        return idx

def order_LCV(pselected,sudoku,pointList):
    ##selects the value which leaves the most choices for other variables
    xpos = pselected.x
    ypos = pselected.y
    #for attempt in pselected.available:
    ## this will be the number that divides into the hash function
    idx = assignIdx(xpos,ypos,sudoku)
    #idx = num for num in range(0,len(sudoku)) if num // 9 == xpos and t2 == num % 9 == ypos else 
    ##order the values by the amount of variables it rules outs
    ruleOutDict = dict()
    for attempt in pselected.available:
        test_sudoku = copy.deepcopy(sudoku)
        test_sudoku[idx] = attempt
        rule_out = checkRuleOut(test_sudoku,pointList)
        ruleOutDict[attempt] = rule_out
         
    ruleOutDict = sorted(ruleOutDict.items(),key=lambda x:x[1],reverse=True)  
    out = [pair[0] for pair in ruleOutDict]
    return out





def checkRuleOut(sudoku, pointList):
    """
    Return the amount of ruled-out values
    :param sudoku:  The modified sudoku where exact a 0-position's value is filled.
    :param pointList: pointList before modification
    :return: Return the amount of ruled-out values
    """
    length = len(sudoku)
    count = 0
    for i in range(length):
        if sudoku[i] == 0:
            p = point(i % 9, i // 9)
            for j in range(1, 10):
                if j not in rowNum(p, sudoku) and j not in colNum(p, sudoku) and j not in blockNum(p, sudoku):
                    count += 1
    oldCount = 0
    for k in pointList:
        oldCount += len(k.available)

    return oldCount - count


def check(p, sudoku):
    """Check if position p's trial value violate rules, return True if not violated"""
    if p.value == 0:
        #print('not assign value to point p!!')
        return False
    if p.value not in rowNum(p, sudoku) and p.value not in colNum(p, sudoku) and p.value not in blockNum(p, sudoku):
        return True
    else:
        return False


def showSudoku(sudoku):
    """Print the sudoku"""
    for j in range(9):
        for i in range(9):
            print('%d ' % (sudoku[j * 9 + i]), end='')
        print('')
    print("\n")

