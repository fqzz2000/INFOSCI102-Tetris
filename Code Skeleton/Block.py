class Block:
    def __init__(self, x:int=0, y:int=0):
        self.shapes = \
            [[[0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 1, 0]],

             [[0, 0, 0, 0],
             [0, 0, 0, 1],
             [1, 1, 1, 1],
             [0, 0, 0, 0]],
             
             [[0, 1, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0]],

              [[0, 0, 0, 0],
               [1, 1, 1, 1],
               [1, 0, 0, 0],
               [0, 0, 0, 0]]]

        self.x = x
        self.y = y
        self.current_direction = 0
        
    # rotate the current block counterclockwise by 90 degree
    def rotateLeft(self)->None:
        # your code here

        return
    
    # move the current block downward by one
    def moveDown(self)->None:
        # your code here

        return
    
    # move the current block rightward by one
    def moveRight(self)->None:
        # your code here
        return
    
    # move the current block leftward by one 
    def moveLeft(self)->None:
        # your code here
        return
    
    # return current shape of the block
    def getShape(self)->"list[list[int]]":
        return self.shapes[self.current_direction]
