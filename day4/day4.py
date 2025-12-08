import copy

class Day4:

    def count_accessisble_roles(self, lines):
        # pos = left, right, top, down, top right, top left, down left, down right
        positions = [(-1, 0), (1, 0), (0, 1), (0, -1),
                    (1, 1), (-1, 1), (-1, -1), (1, -1)]
        count = 0
        h, w = len(lines), len(lines[0])

        for y in range(h):
            for x in range(w):
                if lines[y][x] == '@':
                    adjacents = 0

                    for dx, dy in positions:
                        nx, ny = self.valid_position(dx, dy, x, y, h, w)
                        if nx is None:
                            continue  
                        if lines[ny][nx] == '@':
                            adjacents += 1

                    if adjacents < 4:
                        count += 1

        return count

    def count_accessible_roles_until_no_rolls(self, lines):
        # pos = left, right, top, down, top right, top left, down left, down right
        positions = [(-1, 0), (1, 0), (0, 1), (0, -1),
                    (1, 1), (-1, 1), (-1, -1), (1, -1)]
        count = 0
        h, w = len(lines), len(lines[0])
        grid = [list(row) for row in lines]
        # same as before just 
        for y in range(h):
            for x in range(w):
                if lines[y][x] == '@':
                    adjacents = 0

                    for dx, dy in positions:
                        nx, ny = self.valid_position(dx, dy, x, y, h, w)
                        if nx is None:
                            continue  
                        if lines[ny][nx] == '@':
                            adjacents += 1

                    if adjacents < 4:
                        grid[y][x] = '.'
                        count += 1

        return grid, count
    
    def remove_until_done(self, lines):
        total_removed = 0
        current_grid = lines

        while True:
            new_grid, removed = self.count_accessible_roles_until_no_rolls(current_grid)

            if removed == 0:
                break  # nothing more to remove

            total_removed += removed
            current_grid = ["".join(row) for row in new_grid]  # convert back to strings if needed

        return current_grid, total_removed

    
    

    def valid_position(self, dx, dy, x, y, h, w):
        
        nx = x + dx
        ny = y + dy

        
        if 0 <= nx < w and 0 <= ny < h:
            return nx, ny

        
        return None, None
    

    def get_data(self, file_path: str):
        grid = []

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    
                    grid.append(list(line.strip()))

            return grid
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
