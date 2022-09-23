
##BubblePuzzle Problems

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

p1 = s.BubblePuzzle([["RED","BLUE"],["BLUE","RED"],[],[]])
p2 = s.BubblePuzzle([["RED","ORANGE","BLUE","ORANGE"],["RED","RED","BLUE","BLUE"],["BLUE","RED","ORANGE","ORANGE"],[],[]])
p3 = s.BubblePuzzle([["RED","ORANGE","BLUE","ORANGE"],["RED","RED","BLUE","BLUE"],["BLUE","RED","GREEN","GREEN"],["GREEN","ORANGE","GREEN","ORANGE"],[],[]])
p4 = s.BubblePuzzle([["GREEN","RED","RED","BLUE"],["RED","ORANGE","PURPLE","PURPLE"],["BLUE","GREEN","BLUE","ORANGE"],["ORANGE","RED","ORANGE","GREEN"],["PURPLE","PURPLE","GREEN","BLUE"],[],[]])

probs = [p1,p2,p3,p4]
##generate a heuristic5

for num,prob in enumerate(probs):
        print("\nBUBBLE PUZZLE!!\n")
        print("\nProblem ",num+1,"Initial State ",prob.initial)

        s.makeGlobs()

        print("\nA* Search with Heuristic 3")
        t = time()
        node,n1,n2 = s.astar_search(prob, h = prob.h_Rand,h_test=False,known_true_cost=None, display = True)        
        newt = time()
        print("TESTING HEURISTIC ")
        solution_cost=len(node.solution())
        
        s.astar_search(prob, h = prob.h_Rand,h_test=True,known_true_cost=solution_cost)
        print("Heuristic Test completed")
        timeExec(t,newt)

        s.makeGlobs()

        print("\nGreedy Search with  heuristic 3")
        t = time()
        node,n1,n2 = s.greedy_search(prob, h = prob.h_Rand, display = True)
        newt = time()
        print("TESTING HEURISTIC ")
        solution_cost=len(node.solution())
        s.greedy_search(prob, h = prob.h_Rand,h_test=True,known_true_cost=solution_cost)
        print("Heuristic Test completed")
        timeExec(t,newt)
        s.makeGlobs() 
        
        print("\nA* Search with Heuristic 1")
        t = time()
        node,n1,n2 = s.astar_search(prob, h = prob.h1,h_test=False,known_true_cost=None, display = True)        
        print("TESTING HEURISTIC ")
        solution_cost=len(node.solution())
        s.astar_search(prob, h = prob.h1,h_test=True,known_true_cost=solution_cost)
        print("Heuristic Test completed")
        newt = time()
        timeExec(t,newt)

        s.makeGlobs()

        print("\nGreedy Search with Heuristic 1")
        t = time()
        node,n1,n2 = s.greedy_search(prob, h = prob.h1, display = True)
        newt = time()
        print("TESTING HEURISTIC ")
        solution_cost=len(node.solution())
        s.greedy_search(prob, h = prob.h1,h_test=True,known_true_cost=solution_cost)
        print("Heuristic Test completed")
        timeExec(t,newt)

        s.makeGlobs()

        print("\nA* Search with Heuristic 2")
        t = time()
        node,n1,n2 = s.astar_search(prob, h = prob.h2,h_test=False,known_true_cost=None, display = True)        
        print("TESTING HEURISTIC ")
        solution_cost=len(node.solution())
        s.astar_search(prob, h = prob.h2,h_test=True,known_true_cost=solution_cost)
        print("Heuristic Test completed")
        newt = time()
        timeExec(t,newt)

        s.makeGlobs()

        print("\nGreedy Search with Heuristic 2")
        t = time()
        node,n1,n2 = s.greedy_search(prob, h = prob.h2, display = True)
        newt = time()
        print("TESTING HEURISTIC ")
        solution_cost=len(node.solution())
        s.greedy_search(prob, h = prob.h2,h_test=True,known_true_cost=solution_cost)
        print("Heuristic Test completed")
        timeExec(t,newt)
        s.makeGlobs()
  
