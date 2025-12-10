class Day6:
    
    def solve_math(self, ops, nums):
        h,w = len(nums), len(nums[0])
        count = 0
        for i in range(w):
            col_nums = []
            op = ops[i]
            for j in range(h):
                col_nums.append(nums[j][i])
            count += self.calculate(op, col_nums)
        
        return count
    
    def solve_math_2(self, ops, raw_data):
        
        nums = []
        count = 0
        h, w = len(raw_data), len(raw_data[0])
        op_index = len(ops) - 1
        
        for col in range(w-1, -1, -1):
            num = ''
            for row in range(h):
                digit = raw_data[row][col]
                if digit != ' ' and digit != '\n' :
                    num += digit
                    
            if num != '':
                nums.append(num)

            if col == 0 or (raw_data[0][col] == ' ' and raw_data[0][col-1] != ' '):
                print(nums)
                count += self.calculate(ops[op_index], nums)
                op_index -= 1
                nums = []
                
        return count
            
                    
    def gather_numbers(self, raw_data):
        # read columns from left to write
        h, w = len(raw_data), len(raw_data[0])
        res = []
        for col in range(w-1, -1, -1):
            num = ''
            for row in range(h):
                digit = raw_data[row][col]
                num += digit
            res.append(num)
        
        # delete the first row as it contains only breaking chars
        del res[0]
        
        # fuck this solution just added an empty el so that the group_numbers pushes the last group
        res.append(' ')
        
        return res
    
    def group_numbers(self, raw_numbers):
        numbers = []
        group = []
        
        
        for el in raw_numbers:
            el = el.strip()
            after_strip = len(el)
            
            if after_strip == 0:
                numbers.append(group)
                group = []
            else:
                group.append(int(el))
         
        return numbers
    
    def calculate_2(self, ops, nums):
        index_ops = len(ops)
        count = 0
        for group in nums:
            index_ops -= 1
            count += self.calculate(ops[index_ops], group)
        
        return count
                
            
            
    
    
    def calculate(self, op, nums):
        match op:
            case '+':
                return sum(list(map(int, nums)))
            case '*':
                res = 1
                for num in nums:
                    res *= int(num)
                return res
                        
                        
    
    def get_data(self, file_path):
        numbers = []
        
        
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    numbers.append(line.strip().split())
                
            operations = numbers[-1]
            del numbers[-1]
            return operations, numbers
        except FileNotFoundError as e:
            print('path not found error: ', e)
    
        
        
        
        
    def get_data_2(self, file_path):
        # fuck the cephalopods, no cephalopods should do math
        
        raw_data = []
        ops = []
        
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    raw_data.append(line)
                
            ops = raw_data[-1].strip().split()
            
            del raw_data[-1]
            return ops, raw_data
        except FileNotFoundError as e:
            print('path not found error: ', e)
        
        