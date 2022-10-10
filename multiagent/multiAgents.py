# multiAgents.py
# --------------
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


from util import manhattanDistance
from pacman import GameState
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

# TODO: implement this
class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        return self.minimax_search(gameState)

    # minmax search based on the pseudocode from the 
    def minimax_search(self, gameState: GameState):
        """
        An algorithm for calculating the optimal move using minimax
        """
        depth = 0
        value, move = self.max_value(gameState, depth)
        return move

    
    def max_value(self, gameState: GameState, depth: int):
        # Pacman is always agent 0
        pacman = 0
        actions = gameState.getLegalActions(pacman)
        if self.is_terminal(gameState, actions, depth):
            return (self.evaluationFunction(gameState), None)

        # initialize the value to be the worst possible value
        v = -(float("inf"))
        # bounding the move variable
        move = None

        # for each action, get the value of the successor state
        for action in actions:
            v2, a2 = self.min_value(gameState.generateSuccessor(pacman, action), 1, depth)
            if v2 > v:
                v, move = v2, action
        # return the value and the move
        return v, move


    def min_value(self, gameState: GameState, agent: int, depth: int):
        actions = gameState.getLegalActions(agent)
        if self.is_terminal(gameState, actions, depth):
            return (self.evaluationFunction(gameState), None)
        
        # initialize the value to be the worst possible value
        v = float("inf")
        # bounding the move variable
        move = None
        # go through the whole game tree, all the way to the leaves
        # determine the backed-up value of a state and the move to get there
        for action in actions:
            if agent == gameState.getNumAgents() - 1:
                v2, a2 = self.max_value(gameState.generateSuccessor(agent, action), depth + 1)
            else:
                v2, a2 = self.min_value(gameState.generateSuccessor(agent, action), agent + 1, depth)
            
            if v2 < v:
                v, move = v2, action
            
        return v, move
            
    # check if the game is over or if the depth is reached
    def is_terminal(self, gameState: GameState, actions: list, depth: int) -> bool:
        if len(actions) == 0 or gameState.isWin() or gameState.isLose() or depth == self.depth:
            return True
        else:
            return False



# TODO: implement this
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        return self.alpha_beta_search(gameState)

    def alpha_beta_search(self, gameState: GameState):
        """
        An algorithm for calculating the optimal move using minimax
        """
        alpha = -(float("inf"))  # min
        beta = float("inf") # max
        depth = 0
        value, move = self.max_value(gameState, depth, alpha, beta)
        return move

    def max_value(self, gameState: GameState, depth: int, alpha: float, beta: float):
        # Pacman is always agent 0
        pacman = 0
        # retrieving the legal actions
        actions = gameState.getLegalActions(pacman)
        if self.is_terminal(gameState, actions, depth):
            return (self.evaluationFunction(gameState), None)
        
        # initialize the value to be the worst possible value
        v = -(float("inf"))
        # bounding the move variable
        move = None

        for action in actions:
            v2, a2 = self.min_value(gameState.generateSuccessor(pacman, action), 1, depth, alpha, beta)
            if v2 > v:
                v, move = v2, action
                alpha = max(alpha, v)
            if v > beta:
                return v, move
        return v, move
    
    def min_value(self, gameState: GameState, agent: int, depth: int, alpha: float, beta: float):
        # get the legal actions for the agent/ghost
        actions = gameState.getLegalActions(agent)
        if self.is_terminal(gameState, actions, depth):
            return (self.evaluationFunction(gameState), None)

        # initialize the value to be the worst possible value
        v = float("inf")
        # bounding the move variable
        move = None

        for action in actions:
            if agent == gameState.getNumAgents() - 1:
                v2, a2 = self.max_value(gameState.generateSuccessor(agent, action), depth + 1, alpha, beta)
            else:
                v2, a2 = self.min_value(gameState.generateSuccessor(agent, action), agent + 1, depth, alpha, beta)
            if v2 < v:
                v, move = v2, action
                beta = min(beta, v)
            if v < alpha:
                return v, move
        return v, move

    # check if the game is over or if the depth is reached
    def is_terminal(self, gameState: GameState, actions: list, depth: int) -> bool:
        if len(actions) == 0 or gameState.isWin() or gameState.isLose() or depth == self.depth:
            return True
        else:
            return False


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
