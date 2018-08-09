# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
        '''
        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;
        '''
                            
        def compute_height(self):
            height = 0
            q = []
        
            for i in range(self.n):
                q.append(i)
                nodeCount = len(q)
                
                if nodeCount == 0:
                    return height
                while i != -1:
                    height += 1
                    i = self.parent[i]
                    
                while (nodeCount > 0):
                    # Remove node of this level
                    q.pop(0)
                    # Add node of next level
                    q.append(self.parent[i])
                    nodeCount -= 1
'''
                
            # Read each parent index
            for child_index in range(self.n):
                height = 0
                parent_index = self.parent[child_index]
                if parent_index == -1:
                    self.root = child_index
                    height += 1
                else:
                    nodes[parent_index].append(nodes[child_index])
                    maxHeight = max(maxHeight, height)
            return maxHeight
'''        
        
def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
