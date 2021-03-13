class Results:
    def __init__(self, result, depthSolution, costSolution, expandedNodes, frontierNodes, soluctionNodePath):
        self.result = result
        self.depthSolution = depthSolution
        self.costSolution = costSolution
        self.expandedNodes = expandedNodes
        self.frontierNodes = frontierNodes
        self.solutionNodePath = soluctionNodePath
    