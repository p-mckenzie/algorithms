class Percolation():
    
    def __init__(self, N):
        from quickfind import WeightedQuickUF
        self.N = N
        
        self.base = WeightedQuickUF(n=self.N**2+2)
        self.open = [1] + [0]*self.N**2 + [1]
        
        '''
        # connect top row to the dummy 0th element
        # connect bottom row to the dummy -1th element
        for col in range(self.N):
            self.base.union(col+1, 0)
            self.base.union(self.N**2+1, self.N**2+1-(col+1))
        '''
        
    def Open(self, row, col):
        loc = self.locate(row, col)
        
        self.open[loc] = 1
        
        # connect location to its (open) neighbors
        for offset in range(-1,2):
            try: # row +- 1
                new_loc = self.locate(row+offset, col)
                if self.open[new_loc]:
                    self.base.union(loc, new_loc)
            except:
                continue
                
            try: # column +- 1
                new_loc = self.locate(row, col+offset)
                if self.open[new_loc]:
                    self.base.union(loc, new_loc)
            except:
                continue

        # connect location to top or bottom, if applicable
        if row==1:
            self.base.union(0, loc)
        elif row==self.N:
            self.base.union(self.N**2+1, loc)
        
            
    def isOpen(self, row, col):
        loc = self.locate(row, col)
        
        return self.open[loc]==1
    
    def isFull(self, row, col):
        loc = self.locate(row, col)
        
        # pixel is "full" if it's connected to the top row - represented by our 0th element
        return self.base.find(loc)==self.base.find(0)
    
    def percolates(self):
        return self.base.find(0)==self.base.find(self.N**2+1)
    
    # ----------------- helpers --------------------------------
    
    def locate(self, row, col): # converts row, col to a location (if valid) in the flat array
        try:
            assert 1<=row<=self.N and 1<=col<=self.N
        except:
            raise Exception('User input is invalid. Constrain row, col values to [1,N].')
            
        return (row-1)*self.N+col
    
    def check(self):
        return [self.isFull(row, col) for row in range(1,self.N+1) for col in range(1,self.N+1)]