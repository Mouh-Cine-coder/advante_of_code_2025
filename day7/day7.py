class Day7:
    
    '''
        To solve the first part
        the idea to solve this problem is that we build a grid with beams
        A grid with beams will help us easily find the an event where the beams splits
            this one  ->    |
                            ^
        just a splitter with a beam behind it
        then we count this event hence the answer   
        
        check this https://www.reddit.com/r/adventofcode/comments/1pgnmou/2025_day_7_lets_visualize/ 😶‍🌫️
        
        I am writing comments fuck u if u think an LLM wrote them, you think you're smart ! come fight me hhhhh

    ''' 
    
    
    def build_grid_beam(self, space):
        h, w = len(space), len(space[0])
        
        for row in range(h):
            for col in range(w):
                if row % 2 == 0:
                    # consider only the even rows, because they are the only rows i need to read from (z3ma ra kan optimize odakchi hhh)
                    pos = space[row][col]
                    if pos == 'S':
                        # put the beam right down the source
                        space[row + 1][col] = '|'
                    elif pos == '^':
                        # put beams all the way down starting from the left and right of the splitter until a splitter shows up or a prev beam 
                        i = row
                        while i < h and space[i][col + 1] != '^' and space[i][col + 1] != '|':
                            # right
                            space[i][col + 1] = '|'
                            i += 1
                        i = row 
                        while i < h and space[i][col - 1] != '^' and space[i][col - 1] != '|':
                            # left
                            space[i][col - 1] = '|'
                            i += 1
        return space

    
    def count_splits(self, space):
        h, w = len(space), len(space[0])
        splits = 0
        for row in range(h):
            for col in range(w):
                if row % 2 == 0:
                    pos = space[row][col]
                    up_pos = space[row - 1][col]
                    if pos == '^' and up_pos == '|':
                        splits += 1
            
        return splits
    
    def count_multitimes(self, space):
        # basing this solution on the subreddit animation
        curr = [0] * len(space[0])
        
        h, w = len(space), len(space[0])
        
        for row in range(h):
            for col in range(w):
                if row % 2 == 0:
                    pos = space[row][col]
                    if pos == '^':
                        tmp = curr[col]
                        curr[col + 1] += tmp
                        curr[col - 1] += tmp
                        curr[col] = 0
                    if pos == 'S':
                        curr[col] = 1
        
        return sum(curr)
    
    def get_data(self, file_path):
        data = []
        
        try:
            with open(file_path, 'r') as file:
                # we build a grid as a matrix of and the string should be arrays as we need to mutate later
                data = [list(line.strip()) for line in file]
            
            return data
        except FileNotFoundError as e:
            pass