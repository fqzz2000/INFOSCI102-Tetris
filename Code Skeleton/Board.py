from Block import Block
class Board:
    def __init__(self):
        self.cur_block = Block()
        self.board = [[0] * 20 for _ in range(15)]
    
    # check if current block is valid
    def isBlockValid(self, x:int, y:int)->bool:
        # your code here
        return False
    
    # move the block downward by 1 positon if the move is valid, otherwise do nothing 
    def tryMoveDown(self)->None:
        # your code here
        return

    
    # write current shape to the board permanently
    def dump(self)->None:
        # your code here
        return

    # put a new block on the top of the board
    def putNewBlock(self)->None:
        # your code here
        return
    
    # return the current board with block on it 
    def getView(self)->"list[list[int]]":
        tmp = [self.board[i][:] for i in range(15)]
        for i in range(4):
            for j in range(4):
                if (self.cur_block.x + i < 15 and 
                    self.cur_block.y + j < 20 and 
                    self.cur_block.y + j >= 0 and 
                    self.cur_block.getShape()[i][j] == 1):
                    tmp[self.cur_block.x + i][self.cur_block.y + j] = 1
        return tmp

