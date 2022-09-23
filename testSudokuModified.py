"""
Run individual tests. Methods to be tested are imported from sudoku.py in the same directory as this file.
"""
from solveSudoku import *

def validSudoku(sudoku):
    """Return True if the sudoku is valid, False otherwise"""
    return testSudoku(sudoku)

input_txt=[
    [
        8, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 6, 0, 0, 0, 0, 0,
        0, 7, 0, 0, 9, 0, 2, 0, 0,
        0, 5, 0, 0, 0, 7, 0, 0, 0,
        0, 0, 0, 0, 4, 5, 7, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 3, 0,
        0, 0, 1, 0, 0, 0, 0, 6, 8,
        0, 0, 8, 5, 0, 0, 0, 1, 0,
        0, 9, 0, 0, 0, 0, 4, 0, 0,
    ],
    [
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 6, 0, 0, 0, 0, 0,
        0, 7, 0, 0, 9, 0, 2, 0, 0,
        0, 5, 0, 0, 0, 7, 0, 0, 0,
        0, 0, 0, 0, 4, 5, 7, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 3, 0,
        0, 0, 1, 0, 0, 0, 0, 6, 8,
        0, 0, 8, 5, 0, 0, 0, 1, 0,
        0, 9, 0, 0, 0, 0, 4, 0, 0,
    ],
    [
        0, 1, 0, 0, 0, 0, 7, 0, 0,
        5, 0, 0, 0, 7, 3, 0, 0, 0,
        0, 0, 0, 9, 2, 8, 0, 0, 5,
        0, 0, 3, 0, 4, 0, 0, 8, 6,
        0, 9, 0, 0, 0, 0, 0, 0, 4,
        0, 2, 0, 0, 0, 0, 9, 0, 7,
        0, 8, 0, 0, 0, 2, 0, 0, 1,
        9, 0, 6, 0, 0, 0, 0, 0, 3,
        0, 0, 0, 0, 0, 0, 0, 6, 0,
    ],
    [
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
    ],
    [
        8, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 9, 8, 0, 5, 0, 3,
        0, 1, 0, 0, 0, 0, 8, 0, 2,
        4, 0, 0, 1, 0, 0, 6, 7, 0,
        0, 3, 0, 6, 0, 0, 0, 2, 0,
        0, 0, 9, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 4, 5, 0, 0, 0,
        7, 2, 0, 0, 0, 1, 0, 6, 0,
        0, 0, 0, 0, 0, 0, 2, 0, 0,
    ],[
        0, 0, 0, 0, 0, 3, 0, 0, 9,
        0, 0, 0, 0, 0, 0, 0, 6, 0,
        0, 0, 7, 0, 0, 0, 3, 4, 2,
        0, 0, 0, 5, 1, 0, 0, 0, 0,
        9, 0, 0, 0, 3, 0, 0, 0, 0,
        0, 4, 0, 0, 0, 0, 0, 0, 8,
        3, 0, 0, 2, 6, 7, 0, 9, 0,
        4, 0, 0, 0, 0, 0, 0, 8, 0,
        0, 9, 1, 8, 0, 4, 0, 0, 7,
    ]

]
sudoku_txts=[
        [1, 1, 0, 0, 0, 3, 0, 0, 9,
        0, 0, 0, 0, 0, 0, 0, 6, 0,
        0, 1, 7, 0, 0, 0, 3, 4, 2,
        0, 0, 0, 5, 1, 0, 0, 0, 0,
        9, 0, 0, 0, 3, 0, 0, 0, 0,
        0, 4, 0, 0, 0, 0, 0, 0, 8,
        3, 0, 0, 2, 6, 7, 0, 9, 0,
        4, 0, 0, 0, 0, 0, 0, 8, 0,
        0, 9, 1, 8, 0, 4, 0, 0, 7,],
        [
        2, 1, 8, 9, 6, 7, 5, 4, 3,
        5, 9, 4, 8, 1, 3, 2, 7, 6,
        6, 7, 3, 2, 4, 5, 1, 9, 8,
        7, 4, 9, 1, 2, 6, 3, 8, 5,
        8, 5, 1, 4, 3, 9, 6, 2, 7,
        3, 6, 2, 7, 5, 8, 9, 1, 4,
        1, 8, 6, 3, 7, 2, 4, 5, 9,
        4, 3, 7, 5, 9, 1, 8, 6, 2,
        9, 2, 5, 6, 8, 4, 7, 3, 1,],
        [
        2, 1, 8, 9, 6, 7, 5, 4, 3,
        5, 9, 4, 8, 1, 3, 2, 7, 6,
        6, 7, 3, 2, 4, 5, 1, 9, 8,
        7, 4, 9, 1, 2, 6, 3, 8, 5,
        8, 5, 1, 4, 3, 9, 6, 2, 7,
        3, 6, 2, 7, 5, 8, 9, 1, 4,
        1, 8, 6, 3, 7, 2, 4, 5, 9,
        4, 3, 7, 5, 9, 1, 8, 6, 2,
        9, 2, 5, 6, 8, 4, 7, 3, 4,],
        [
        2, 1, 8, 9, 6, 7, 5, 4, 3,
        5, 9, 4, 8, 1, 3, 2, 7, 6,
        6, 7, 3, 2, 4, 5, 1, 9, 8,
        7, 4, 9, 1, 2, 6, 3, 8, 5,
        8, 5, 1, 4, 3, 9, 6, 2, 7,
        3, 6, 2, 7, 5, 8, 9, 1, 4,
        1, 8, 6, 3, 7, 2, 4, 5, 9,
        4, 3, 7, 5, 9, 1, 8, 6, 2,
        9, 2, 5, 6, 8, 4, 7, 3, 3,]
]
results_txt={
    "MRV":[153,71,527,81,63,220],
    "default":[164,165,29712,389,29736,1700],
    "New":[2875,7146,2847,451,4447,8973]
}
def test_method():
    #test the testSudoku methods
    matched=0
    for sudoku in sudoku_txts:
        if validSudoku(sudoku)==testSudoku(sudoku):
            matched+=1
    return matched

def test_all():
    # test your testSudoku methods
    if test_method()==len(sudoku_txts):
        print("Yes, correct testSudoku method.")
    else:
        print("No, incorrect testSudoku method.")
    matched=0
    for select in ["MRV","New"]: ##selection of heuristics
        for sudoidx in range(len(input_txt)):
            sudo=input_txt[sudoidx]
            sudoku=copy.deepcopy(sudo)
            if validSudoku(sudoku):
                print("Puzzle is Valid. Now finding a solution") 
            else: 
                print("Not a valid Puzzle.") 
                continue
            
            pointList = initPoint(sudoku)
            print("=============No.%d test begin================"%(sudoidx+1))
            if BacktrackCSP_frameWork(pointList, sudoku,select=select): print("YES, program runs well")
            
            if sc.steps<=results_txt[select][sudoidx]:
                matched+=1
                print("Yes, solution found in %d steps"%sc.steps)
            else: print("No.of steps %d is too high"%sc.steps)
            
            print("==============tests end===============")
    
    print("totally %d solutons are found."%matched)
 
if __name__ == '__main__':
    test_all()

