class WeightedQuickUF():
    
    def __init__(self, n=10):
        '''initializes empty union-find data structure'''
        self.ids = list(range(n))
        self.heights = [0 for item in range(n)]
        
    def count(self):
        '''returns the number of sets'''
        return len(set([self.find(s) for s in range(len(self.ids))]))
    
    def find(self, p):
        '''returns the root element of element p'''
        root = self.ids[p]
        while root!=self.ids[root]:
            root = self.ids[root]
            
        # loop again, setting ids[element] = root for every element 
        ## (two-pass path compression)
        element = p
        while element!=root:
            next_element = self.ids[element]
            self.ids[element] = root
            self.heights[element] = 1
            
            element = next_element
            
        return root
    
    def union(self, p, q):
        '''merges the set containing p with the set containing q'''
        root_p = self.find(p)
        root_q =self.find(q)
        
        if self.heights[p]>self.heights[q]:
            self.ids[root_q] = root_p
            self.heights[q] += 1
        else:
            self.ids[root_p] = root_q
            self.heights[p] += 1
        return
    
    def main(self, stdin):
        '''reads a sequence of pairs of integers from standard input, merges them'''
        
        for (p,q) in stdin:
            self.union(p,q)
            print(p,q)