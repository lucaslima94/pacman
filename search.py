# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    from game import Directions
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    goalStatetest=False
    contador=0
    listaEstados=[]
    listaDirecoes=[]
    listavisitados=[]
    listapai=[]
    listaindex=[]
    atualState=problem.getStartState()
    listaEstados.append(atualState)
    listaDirecoes.append(Directions.STOP)
    listapai.append(None)
    south=Directions.SOUTH
    north=Directions.NORTH
    east=Directions.EAST
    west=Directions.WEST
    stop=Directions.STOP
    # enquanto nao encontrar estado final, faz sequencia de operacoes
    while(goalStatetest==False):
		# estado atual recebe proximo estado da lista de estados
		atualState=listaEstados[contador]
		print atualState
		# testa se estado atual esta na lista de estados visitados
		# se sim nao faz nada
		if atualState in listavisitados:
			contador=contador+1
		# senao realiza operacoes
		else:
			# gera uma lista de sucessores
			sucessorList= problem.getSuccessors(atualState)
			# cria uma lista dedirecoes com a direcao de cada sucessor
			for i in  range(0,len(sucessorList)):
				listaEstados.append(sucessorList[i][0])
				if(sucessorList[i][1]=='South'):	
					listaDirecoes.append(south)
					listapai.append(contador)
				elif (sucessorList[i][1]=='North'):
					listaDirecoes.append(north)
					listapai.append(contador)
				elif (sucessorList[i][1]=='East'):
					listaDirecoes.append(east)
					listapai.append(contador)
				elif (sucessorList[i][1]=='West'):
					listaDirecoes.append(west)
					listapai.append(contador)
			contador=contador+1
			#booleno recebe teste para saber se chegou no estado final
			goalStatetest=problem.isGoalState(atualState)
			print goalStatetest
			
		#adiciona estado atual na lista de estados visitados
		listavisitados.append(atualState)
    contador=contador-1
    print contador
    print listaEstados[contador]
    print listaDirecoes[contador]
    paiatual=listapai[contador]
    listaindex.append(paiatual)
    while listapai[paiatual]!=0:
		paiatual=listapai[paiatual]
		listaindex.append(listapai[paiatual])
    listaindex2=listaindex[::-1]
    caminho=[]
    for j in range (0,len(listaindex2)):
		caminho.append(listaDirecoes[listaindex2[j]])
    caminho.append(listaDirecoes[contador])
    caminho.append(listaDirecoes[contador+1])
    print "tamanho lista estados",len(listaEstados)	 
    print "tamanho lista de direcoes",len(listaDirecoes)
    return caminho
    

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
