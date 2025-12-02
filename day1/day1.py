class Day1:
    
    
    def dial_at_zero_1(self, data):
        res = 0
        curPos = 50
        
        for ins in data:
            sign, rn = self.read_instruction(ins)
            
            curPos = curPos + (sign * rn)
            
            if curPos % 100 == 0:
                res += 1
        
        return res

    def dial_at_zero_2(self, data):
        res = 0
        curPos = 50
        
        for ins in data:
            sign, rn = self.read_instruction(ins)
            
            for _ in range(rn):
                curPos = curPos + sign
                if curPos % 100 == 0:
                    res += 1
            
        
        return res
    
    
    def read_instruction(self, value: str):
        direction = value[0]
        
        if direction == 'L':
            sign = -1
        elif direction == 'R':
            sign = 1
        
        rotation_number = int(value[1::])
        
        return [sign, rotation_number]
    
    
    def get_data(self, file_path: str):
        data = []
        
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    data.append(line.strip())
            return data
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        
