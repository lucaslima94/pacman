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
import copy

def manhattanHeuristic(atualstate,finalstate):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = atualstate
    xy2 = finalstate
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

class estado(object):
	position,direction,father,gx,fx,hx,visitorstatus,profundidade=None,None,None,None,None,None,None,None
	
	def setposition(self,x):
		self.position=x
	
	
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
    #return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    from game import Directions
    #cria variaveis para as direcoes
    south=Directions.SOUTH	
    north=Directions.NORTH
    east=Directions.EAST
    west=Directions.WEST
    stop=Directions.STOP
    #lista de objetos onde sao armazenados os estados
    listaestados=[]
    #lista de estados visitados
    listavisitados=[]
    #lista para o caminho do estado incial ate o final
    caminho=[]
    contador=0
    #booleano q indica se e o estao final
    finalstatetest=False
    
    #cria um objeto inicial, q recebe o estado inicial do problema, joga esse estado na listaestados
    atualstate=estado()
    originalstate=estado()
    atualstate.position=problem.getStartState()
    atualstate.direction=stop
    atualstate.father=None
    listaestados.append(copy.copy(atualstate))
    #enquanto nao encontra estado final
    while(finalstatetest==False):
		#estado atual recebe n-esimo estado do vetor
		atualstate=copy.copy(listaestados[contador])
		#testa se estado ja foi visitado
		if atualstate.position in listavisitados:
			contador = contador +1
		else:
			#se nao gera filhos deste estado
			originalstate=copy.copy(atualstate)
			sucessorlist=problem.getSuccessors(atualstate.position)
			for i in range(0,len(sucessorlist)):
				#inicializa filhos e coloca na listaestados
				atualstate.position=sucessorlist[i][0]
				atualstate.father=contador
				heuristica=manhattanHeuristic(atualstate.position,problem.goal)
				if(sucessorlist[i][1]=='South'):
					atualstate.direction=south
					listaestados.append(copy.copy(atualstate))
					
				elif(sucessorlist[i][1]=='North'):
					atualstate.direction=north
					listaestados.append(copy.copy(atualstate))
					
				elif(sucessorlist[i][1]=='West'):
					atualstate.direction=west
					listaestados.append(copy.copy(atualstate))
					
				elif(sucessorlist[i][1]=='East'):
					atualstate.direction=east
					listaestados.append(copy.copy(atualstate))
					
				elif(sucessorlist[i][1]=='Stop'):
					atualstate.direction=stop
					listaestados.append(copy.copy(atualstate))
			#incrementa contador
			contador=contador+1	
		#testa se o estado atual e um estado final	
		finalstatetest=problem.isGoalState(originalstate.position)
		listavisitados.append(copy.copy(originalstate.position))
    	
    atualstate=copy.copy(listaestados[contador-1])
    caminho.append(copy.copy(atualstate.direction))
    while(atualstate.father!=None):
		atualstate=copy.copy(listaestados[atualstate.father])
		caminho.append(copy.copy(atualstate.direction))
		caminho2=caminho[::-1]
    
        
    		
    finalstate=problem.goal
    print problem.goal
    return caminho2
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



def hillClimbing(problem, heuristic=nullHeuristic):
	from game import Directions
	import copy
	#cria variaveis para as direcoes
	south=Directions.SOUTH	
	north=Directions.NORTH
	east=Directions.EAST
	west=Directions.WEST
	stop=Directions.STOP
	
	statelist=[]
	listavizinhos=[]
	
	goalstatetest=False
	initialstate=estado()
	atualstate=estado()
	originalstate=estado()
	initialstate.position=problem.getStartState()
	initialstate.direction=stop
	initialstate.father=None
	initialstate.fx=manhattanHeuristic(initialstate.position,problem.goal)
	initialstate.visitorstatus=-1
	initialstate.profundidade=0
	statelist.append(copy.copy(initialstate))
	
	atualstate=copy.copy(statelist[0])
	originalstate=copy.copy(atualstate)
	
	for i in range(0,1000):
	
		listavizinhos=[]
		sucessorlist=problem.getSuccessors(atualstate.position)
		for i in range(0,len(sucessorlist)):
			atualstate.position=sucessorlist[i][0]
			#atualstate.father=smallestindex
			atualstate.fx=manhattanHeuristic(sucessorlist[i][0],problem.goal)
			atualstate.visitorstatus=-1
			atualstate.profundidade=originalstate.profundidade+1
			if(sucessorlist[i][1]=='South'):
				atualstate.direction=south
				statelist.append(copy.copy(atualstate))
				listavizinhos.append(copy.copy(atualstate))
			elif(sucessorlist[i][1]=='North'):
				atualstate.direction=north
				statelist.append(copy.copy(atualstate))
				listavizinhos.append(copy.copy(atualstate))
			elif(sucessorlist[i][1]=='West'):
				atualstate.direction=west
				statelist.append(copy.copy(atualstate))
				listavizinhos.append(copy.copy(atualstate))
			elif(sucessorlist[i][1]=='East'):
				atualstate.direction=east
				statelist.append(copy.copy(atualstate))
				listavizinhos.append(copy.copy(atualstate))
			elif(sucessorlist[i][1]=='Stop'):
				atualstate.direction=stop
				statelist.append(copy.copy(atualstate))
				listavizinhos.append(copy.copy(atualstate))
		for i in range(0, len(statelist)):
			if ((originalstate.profundidade==statelist[i].profundidade) and (originalstate.position != statelist[i].position )):
				listavizinhos.append(copy.copy(statelist[i]))
		
		for i in range(0,len(listavizinhos)):
			if (listavizinhos[i].fx<=originalstate.fx):
				originalstate=copy.copy(listavizinhos[i])
    
    
	for i in range(0,len(listavizinhos)):
		print listavizinhos[i].position
	
	print "original",originalstate.position
	return [stop]
	util.raiseNotDefined()


def aStarSearch(problem, heuristic=nullHeuristic):
    from game import Directions
    #cria variaveis para as direcoes
    south=Directions.SOUTH	
    north=Directions.NORTH
    east=Directions.EAST
    west=Directions.WEST
    stop=Directions.STOP
    
    listaestados=[]
    caminho=[]
    listavisitados=[]
    smalleststate=estado()
    smallestindex=-1
    atualstate=estado()
    goalstatetest=False
    
    initialstate=estado()
    initialstate.position=problem.getStartState()
    initialstate.direction=stop
    initialstate.father=None
    initialstate.gx=1
    initialstate.hx=manhattanHeuristic(initialstate.position,problem.goal)
    initialstate.fx=initialstate.gx+initialstate.hx
    initialstate.visitorstatus=-1
    
    listaestados.append(copy.copy(initialstate))
    while (goalstatetest==False):
		for i in range(0,len(listaestados)):
			if (listaestados[i].visitorstatus==-1):
				smalleststate=copy.copy(listaestados[i])
				smallestindex=i
				break
		
		for i in range(0,len(listaestados)):
			if((listaestados[i].fx < smalleststate.fx) and listaestados[i].visitorstatus==-1):
				smalleststate=copy.copy(listaestados[i])
				smallestindex=i
		listaestados[smallestindex].visitorstatus=1
				
		if(smalleststate.position not in listavisitados):
			sucessorlist=problem.getSuccessors(smalleststate.position)
			for i in range(0,len(sucessorlist)):
				atualstate.position=sucessorlist[i][0]
				atualstate.father=smallestindex
				atualstate.gx=smalleststate.gx+1
				atualstate.hx=manhattanHeuristic(sucessorlist[i][0],problem.goal)
				atualstate.fx=atualstate.gx+atualstate.hx
				atualstate.visitorstatus=-1
				if(sucessorlist[i][1]=='South'):
					atualstate.direction=south
					listaestados.append(copy.copy(atualstate))
				elif(sucessorlist[i][1]=='North'):
					atualstate.direction=north
					listaestados.append(copy.copy(atualstate))
				elif(sucessorlist[i][1]=='West'):
					atualstate.direction=west
					listaestados.append(copy.copy(atualstate))
				elif(sucessorlist[i][1]=='East'):
					atualstate.direction=east
					listaestados.append(copy.copy(atualstate))
				elif(sucessorlist[i][1]=='Stop'):
					atualstate.direction=stop
					listaestados.append(copy.copy(atualstate))
			goalstatetest=problem.isGoalState(smalleststate.position)
			listavisitados.append(smalleststate.position)
    
    atualstate=copy.copy(listaestados[smallestindex])
    caminho.append(copy.copy(atualstate.direction))
    while(atualstate.father!=None):
		atualstate=copy.copy(listaestados[atualstate.father])
		caminho.append(copy.copy(atualstate.direction))
    caminho2=caminho[::-1]
    print caminho2
    
    return caminho2
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
hlc = hillClimbing
