class PercolationStats():

    # perform independent trials on an n-by-n grid
    def PercolationStats(self):
        from percolation import Percolation
        from random import randint
        
        self.scores = []
        
        for i in range(self.trials):
            grid = Percolation(N=self.n)

            # open random location until the graph percolates
            while not grid.percolates():
                grid.Open(randint(1,self.n),
                         randint(1, self.n))
                
            # save the # of squares that were "open" when the grid first percolated
            self.scores.append(sum(grid.open[1:-1])/(self.n**2))
            
        # generate aggregate statistics
        from numpy import mean, std
        # sample mean of percolation threshold     
        self.mean = mean(self.scores)
        # sample standard deviation of percolation threshold
        self.stddev = std(self.scores)
        
        # get high and low endpoints of 95% confidence interval
        import numpy as np, scipy.stats as st
        self.confidenceLo, self.confidenceHi = st.t.interval(0.95, len(self.scores)-1, 
                                                             loc=np.mean(self.scores), scale=st.sem(self.scores))
        
        return

    def __init__(self, n, trials):
        try:
            assert n>0 and trials>0
        except AssertionError:
            raise Exception("Input is invalid. n and trials must be greater than zero.")
            
        self.n = n
        self.trials = trials
        
        from random import seed
        seed(1)
        
        self.grid = self.PercolationStats()