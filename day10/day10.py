import regex as re
import functools

class Day10:
    
    def part_one(self, machines):
        ans = 0
        
        for mc in machines:
            
            # global variables
            target, buttons, _ = mc
            
            @functools.cache
            def solve(state, pressed):
                
                if state == target:
                    return 0
                
                
                if pressed > len(state):
                    return 10000000000000
                    
                best = 10000000000000
                
                for btn in buttons:
                    new_state = list(state)

                    for i in btn:
                        # just toggling
                        new_state[i] = '.' if new_state[i] == '#' else '#'
                
                    result = 1 + solve("".join(new_state), pressed + 1)
                    best = min(result, best)
                
                return best
            
            ans += solve("." * len(target), 0)
        
        return ans
    
                

    def get_data(self, file_path):
        try:
            machines = []

            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    # print('\n\n\n' + line)
                    # example  => [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
                    indicators = re.search("\\[(#|.)*\\]", line)
                    if indicators:
                        indicators = indicators.group()[1: -1]

                    # we should gather all the buttons
                    buttons = re.findall(r"\(\d+(?:,\d+)*\)", line)
                    new_buttons = []
                    for btn in buttons:
                        btn = list(map(int, btn[1: -1].split(',')))
                        new_buttons.append(btn)
                    
                        
                    
                    joltage = re.search(r"\{\d+(?:,\d+)*\}", line)
                    if joltage:
                        joltage = tuple(map(int, joltage.group()[1: -1].split(',')))

                    # print("indicators ===> ", indicators)
                    # print("buttons ===> ", buttons)
                    # print("joltage ===> ", joltage)

                    machines.append((indicators, new_buttons, joltage))

            return machines

        except FileNotFoundError as e:
            print(f"file not found Error {e}")
