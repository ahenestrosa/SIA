import math



def getPrimeFunction(beta, func):
    if func == 'tanh':
        def g(x):
            return math.tanh(beta * x)
        def gPrime(x):
            return g(x) * (1-g(x))
    elif func == 'logistic':
        def g(x):
            return 1 / (1 + math.exp(-2* beta * x))
        def gPrime(x):
            exponential = math.exp(-2* beta*x)
            return 2* beta* exponential / (1 + exponential) ** 2  
    return g, gPrime

