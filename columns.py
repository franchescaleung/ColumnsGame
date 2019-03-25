## columns.py

import sys
NONE = '   '


class GameState:
    def __init__(self, num_of_row: int, num_of_col: int):
        self.board = []
        self.num_of_row = int(num_of_row)
        self.num_of_col = int(num_of_col)
        self.temp_faller = ''
        self.last_board = self.board

    def new_game(self) -> [[str]]:
        '''makes new game with specified number of rows and columns'''
        for col in range(self.num_of_col):
            self.board.append([])
            for row in range(self.num_of_row):
                self.board[-1].append(NONE)
        self.last_board = self.board

    def content_game(self, content: [[str]]) -> [[str]]:
        '''creates board with content'''
        for col in range(self.num_of_col):
            self.board.append([])
        for l in content:
            for item in range(len(l)):
                if l[item] != ' ':
                    self.board[item].append(' ' + l[item] + ' ')
        for li in content:
            for i in range(len(li)):
                while len(self.board[i]) != self.num_of_row:
                    self.board[i].insert(0, "   ")
        



    def check_for_matches(self, x: int, y: int, row: int, col: int):
        '''check for matches and adds it to a match list'''
        board = self.board
        color = board[col][row][1]
        match_list = []
        if color != "   " or " ":
            while row < (self.num_of_row) and col < (self.num_of_col) \
                  and board[col][row][1] == color:
                
                match_list.append((col, row))
                row += y
                col += x

            if len(match_list) >= 3:
                return match_list
        
       

    def clear_matches_off_board(self, match_list: 'list of matches'):
       
        for row in range(self.num_of_row):
            for gems in range(self.num_of_col):
                if (gems, row) in match_list:
                    self.board[gems][row] = "   "

        temp_board = []
        for col in range(self.num_of_col):
            temp_board.append([])
            for every_row in range(len(self.board[col])):
                if self.board[col][every_row] !="   ":
                    temp_board[col].append(self.board[col][every_row])
        for l in range(len(temp_board)):
            while len(temp_board[l]) != self.num_of_row:
                temp_board[l].insert(0, "   ")

        
        self.board = temp_board

    def complete_check_and_remove(self):
        match_list = []
        for i in range(self.num_of_col):
            for j in range(self.num_of_row):
                for a in [(1, 0), (0, 1), (1,1), (1, -1)]:
                    temp = self.check_for_matches(a[0], a[1], j, i)
                    if temp != None:
                        match_list.extend(temp)
        self.clear_matches_off_board(match_list)
                    
    def create_faller(self, column: int, three_gems: str):
        #creates fallers with input from ui
        self.temp_faller = fallers(three_gems, column, self)
    


class fallers:
    def __init__(self, three_gems: [str], column_num: int, state: GameState):
        self.types = three_gems
        self.position = [(int(column_num), -3), (int(column_num), -2), (int(column_num), -1)]
        self._direction = 'down'
        self._gamestate = state
        self._state = 'moving'
        
    def change_direction(self, direction: str):
        '''change direction of faller'''
        self._direction = direction
        
    def check_if_landed(self):
        pieces = ['R', 'O', 'G', 'B', 'Y', 'P', 'W']
        row = self.position[-1][1]
        col = self.position[-1][0] - 1
        if self.position[-1][-1] == len(self._gamestate.board[0]) - 1:
            self._state = 'frozen'
        

    def after_landing(self):
        '''if state is frozen, changes state to permanent'''
        if self._state == 'frozen':
            self._state = 'permanent'
    def move(self):
        '''shifts toward direction by one'''
        if self._direction == 'right' and self._state == 'moving':
            try:
                if self._gamestate.board[self.position[-1][0]][self.position[-1][1]] == "   ":
                    for gem in range(len(self.position)):
                        temp = list(self.position[gem])
                        temp[0] += 1
                        row = temp[1]
                        self.position[gem] = tuple(temp)
                        if int(temp[0]) > self._gamestate.num_of_col:
                            game_over()
                        elif row >= 0:
                            #temp[0] is col
                            #temp[1] is row
    
                            self._gamestate.board[int(temp[0])-1][int(temp[1])] = "[" + self.types[gem] + "]"
                            self._gamestate.board[int(temp[0])-2][int(temp[1])] = "   "
            except IndexError:
                pass #board will stay the same


        elif self._direction == 'left' and self._state == 'moving':
            try:
                if self._gamestate.board[self.position[-1][0]-2][self.position[-1][1]] == "   ":
                    for gem in range(len(self.position)):
                        temp = list(self.position[gem])
                        temp[0] -= 1
                        row = temp[1]
                        self.position[gem] = tuple(temp)
                        if int(temp[0]) <= 0:
                            temp = list(self.position[gem])
                            temp[0] += 1
                            self.position[gem] = tuple(temp)
                            
                        elif row >= 0:
                            self._gamestate.board[int(temp[0])-1][int(temp[1])] = "[" + self.types[gem] + "]"
                            self._gamestate.board[int(temp[0])][int(temp[1])] = "   "
            except IndexError:
                pass #board will stay the same

        elif self._direction == 'right' and self._state == 'frozen':
            try:
                if self._gamestate.board[self.position[-1][0]][self.position[-1][1]] == "   ":
                    for gem in range(len(self.position)):
                        
                        temp = list(self.position[gem])
                        temp[0] += 1
                        row = temp[1]
                        self.position[gem] = tuple(temp)
                        if int(temp[0]) > self._gamestate.num_of_col:
                            game_over()
                        elif row >= 0:
                            #temp[0] is col
                            #temp[1] is row
                            self._gamestate.board[int(temp[0])-1][int(temp[1])] = "|" + self.types[gem] + "|"
                            self._gamestate.board[int(temp[0])-2][int(temp[1])] = "   "
                
            except IndexError:
                pass 

        elif self._direction == 'left' and self._state == 'frozen':
            try:
                if self._gamestate.board[self.position[-1][0-2]][self.position[-1][1]] == "   ":

                    for gem in range(len(self.position)):
                        temp = list(self.position[gem])
                        temp[0] -= 1
                        row = temp[1]
                        self.position[gem] = tuple(temp)
                        #col = self.position[gem][0]
                        if int(temp[0]) < 0:
                            game_over()
                        elif row >= 0 and temp[0] > 0:
                            self._gamestate.board[int(temp[0]-1)][int(temp[1])] = "|" + self.types[gem] + "|"
                            self._gamestate.board[int(temp[0])][int(temp[1])] = "   "
                        
                            

            except IndexError:
                pass #stay same
        elif self._direction == 'down' and self._state == 'frozen':
            self.after_landing()
            for gem in range(len(self.position)):
                temp = list(self.position[gem])
                
                if temp[1] >= 0 and temp[0]>0:
                    self._gamestate.board[int(temp[0])-1][int(temp[1])] = " " + self.types[gem] + " "
                elif temp[0] == 0:
                    self._gamestate.board[int(temp[0])][int(temp[1])] = " " + self.types[gem] + " "

        elif self._direction == 'down' and self._state == 'moving':
            try:
                if self._gamestate.board[self.position[-1][0]-1][self.position[-1][1]+1] == "   ":

                    for gem in range(len(self.position)):
                        temp = list(self.position[gem])
                        row = int(temp[1])
                        col = int(temp[0])
                        if row < -1:
                            temp[1] +=1
                            self.position[gem] = tuple(temp)
                        if row == -1:
                            temp[1] +=1
                            self.position[gem] = tuple(temp)
                            self._gamestate.board[int(temp[0])-1][int(temp[1])] = "[" + self.types[gem] + "]"
                            
                        if row >= 0:

                            temp[1] += 1
                            self.position[gem] = tuple(temp)
                            self.check_if_landed()
                            if self._state == 'frozen':
                                for gem in range(len(self.position)):
                                    temp = list(self.position[gem])
                                    self._gamestate.board[int(temp[0])-1][int(temp[1]) ] = "|" + self.types[gem] + "|"
                                self._gamestate.board[int(self.position[0][0]-1)][int(self.position[0][1])-1] = "   "


                            else:
                                self._gamestate.board[int(temp[0])-1][int(temp[1])] = "[" + self.types[gem] + "]"
                                if row > 1:
                                    self._gamestate.board[int(self.position[0][0]) -1][int(self.position[0][1])-1] = "   "
                            
                else:
                    self._state = 'frozen'
                    for gem in range(len(self.position)):
                        temp = list(self.position[gem]) #changed to list so we can change the list

                        row = int(temp[1])
                        col = int(temp[0])
                        if row >= 0:
                            self._gamestate.board[col-1][row] = "|" + self.types[gem] + "|"

            except IndexError:
                pass #board stays the same


            
    def rotates(self) -> None:
        '''switches order of gems/list of gems'''
        gems = self.types #a list of the gems
        temp_gem_list = [gems[2], gems[0], gems[1]]
        self.types = temp_gem_list
        for gem in range(len(self.position)):
            col = self.position[gem][0]
            row = self.position[gem][1]
            if row >= 0 and self._state == 'moving':
                self._gamestate.board[int(col)-1][int(row)] = "[" + self.types[gem] + "]"
            elif row >=0 and self._state == 'frozen':
                self._gamestate.board[int(col)-1][int(row)] = "|" + self.types[gem] + "|"

    def see_if_game_is_over(self) -> bool:
        '''if gem already exists on board in the space below while state is permanent, return True'''
        count = 0
        for gem in range(len(self.position)):
            temp = list(self.position[gem]) #changed to list so we can change the list
            row = int(temp[1]) #changes item in tuple to int
            col = int(temp[0]) #same as above
            if self._state == 'permanent' and row < 0:
                count += 1
                
            if count > 0:
                return True
        return False
    


def game_over():
    '''game over'''
    print("Game Over")
    sys.exit()
