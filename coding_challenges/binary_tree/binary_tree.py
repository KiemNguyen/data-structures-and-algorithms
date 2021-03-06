class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            # Insert a Node
            # then put existing child down 1 level
            t = BinraryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t 
            
    
    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.righChild = self.rightChild
            self.rightChild = t
    
    def getLeftChild(self):
        return self.leftChild        
   
    def getRightChild(self):
        return self.rightChild
    
    def setRootVal(self, obj):
        self.key = obj
        
    def getRootVal(self):
        return self.key
    
r = BinaryTree('a')
r.getRootVal()
print(r.getLeftChild())
r.insertLeft('b')
r.getLeftChild().getRootVal()
        