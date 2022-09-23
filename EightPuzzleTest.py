##Eight Puzzle Probelms
import search as s
import random
from time import time

#from test_search import *
random.seed("aima-python")

def timeExec(t1,t2,display=True):
    diff = abs(t2-t1)
    if display:
        print("executed in {0:.5f} Seconds".format(diff))
    return diff

def runWAstar(problem,weight,h=None,display=True,h_test=False,known_true_cost=None):
    """given a defined problem, run a Weighted A* Traversal Algorithm"""
    print("\nProblem: ",problem.initial)
    print("\n wA* with Heuristic {0}".format(s.name(h)))
    print("\nwith weight {0}:".format(w))
    s.makeGlobs()
    t = time() ##timing the exectuion of the 
    node,n1,n2 = s.wastar_search(problem,h,display,h_test,known_true_cost,w)    
    newt = time()
    timeExec(t,newt)
    return node,n1,n2

##defining the problems
probs = [s.EightPuzzle((1,2,3,4,0,6,7,5,8)),s.EightPuzzle((2,3,6,1,0,4,7,5,8)),s.EightPuzzle((5,3,6,2,0,7,1,4,8)),s.EightPuzzle((1,5,6,3,4,8,0,2,7)),s.EightPuzzle((3,2,5,6,8,4,0,7,1))]
weights = [1,2,10,100]

##for each problem
for num,prob in enumerate(probs):
        print("\nProblem ",num+1," ",prob.initial)
        s.makeGlobs()
        print("\nA* Search with Missing Tile")
        t = time()
        node,n1,n2 = s.astar_search(prob, h = prob.h_MT,h_test=False,known_true_cost=None, display = True)        
        print("TESTING HEURISTIC ")
        solution_cost=len(node.solution())
        s.astar_search(prob, h = prob.h_MT,h_test=True,known_true_cost=solution_cost)
        print("Heuristic Test completed")
        newt = time()
        timeExec(t,newt)

        s.makeGlobs()

        print("\nGreedy Search with Missing Tile")
        t = time()
        s.greedy_search(prob, h = prob.h_MT, display = True)
        newt = time()
        
        s.makeGlobs()
        
        print("\nA* Search with Manhattan Distance")
        t = time()
        node,n1,n2 = s.astar_search(prob, h = prob.h_Man,h_test=False,known_true_cost=None, display = True)        
        print("TESTING HEURISTIC ")
        solution_cost=len(node.solution())
        s.astar_search(prob, h = prob.h_Man,h_test=True,known_true_cost=solution_cost)
        print("Heuristic Test completed")
        newt = time()
        timeExec(t,newt)

        s.makeGlobs()

        print("\nGreedy Search with Manhattan Distance")
        t = time()
        s.greedy_search(prob, h = prob.h_Man, display = True)
        newt = time()

        # print("\nUCS")
        # s.uniform_cost_search(prob,display=True)
        #print("\nMoveCostSearch")
        #s.move_cost_search(prob,display=True)
        
        print("Weighted A*")
        
        for w in weights:
            ##run with different heuristics
            n,solLen,nExp = runWAstar(prob,w,h=prob.h_Man)
            n,solLen,nExp = runWAstar(prob,w,h=prob.h_MT)

        s.makeGlobs()

        print("\nA* Search with H_Rand")
        t = time()
        node,n1,n2 = s.astar_search(prob, h = prob.h_Rand,h_test=False,known_true_cost=None, display = True)        
        print("TESTING HEURISTIC ")
        solution_cost=len(node.solution())
        s.astar_search(prob, h = prob.h_Rand,h_test=True,known_true_cost=solution_cost)
        print("Heuristic Test completed")
        newt = time()
        timeExec(t,newt)

        s.makeGlobs()

        print("\nGreedy Search with H_Rand")
        t = time()
        s.greedy_search(prob, h = prob.h_Rand, display = True)
        newt = time()
         
