class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tempNine = []
        validOrd = [i for i in range(ord('1'),ord('9')+1)]
        validOrd.append(ord('.'))
        numOrd = [i for i in range(ord('1'),ord('9')+1)]
        tempTop = []
        tempMid = []
        tempBot = []
        
        #rows:
        #ord("1") = 49
        #ord("9") = 57
        #ord(".") = 46
        for row in range(9):
            for num in board[row]:
                # print(ord(num))
                if len(num) > 1 or ord(num) not in validOrd:
                    print("ONE")
                    return False
                if ord(num) in numOrd:
                    # print(num)
                    if int(num) in tempNine:
                        print("TWO")
                        return False
                    else:
                        tempNine.append(int(num))
            tempNine = []
            
            for col in range(9):
                if len(board[col][row]) > 1 or ord(board[col][row]) not in validOrd:
                    print("Three")
                    return False
                if ord(board[col][row]) in numOrd:
                    if int(board[col][row]) in tempNine:
                        print("Four")
                        return False
                    else:
                        # print(int(board[col][row]))
                        tempNine.append(int(board[col][row]))
                        # print(tempNine)
                        
                    if col < 3:
                        if int(board[col][row]) in tempTop:
                            print("Five")
                            return False
                        else:
                            tempTop.append(int(board[col][row]))
                    elif col >=3 and col < 6:
                        if int(board[col][row]) in tempMid:
                            # print(tempTop)
                            # print(col)
                            # print(row)
                            # print(int(board[col][row]))
                            print("Six")
                            return False
                        else:
                            tempMid.append(int(board[col][row]))
                    else:
                        if int(board[col][row]) in tempBot:
                            print("Seven")
                            return False
                        else:
                            tempBot.append(int(board[col][row]))
            tempNine = []
            
            if row % 3 == 2:
                # print(tempNine)
                print(tempTop)
                # print(tempMid)
                # print(tempBot)
                tempTop = []
                tempMid = []
                tempBot = []
                
        
        
            
        return True

            