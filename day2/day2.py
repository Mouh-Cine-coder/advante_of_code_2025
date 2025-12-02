class Day2:
    
    
    def invalid_ids_1(self, ranges):
        res = 0
        
        for rg in ranges:
            start, end = self.get_range(rg)
            for i in range(start, end):
                if self.is_invalid_1(i):
                    res += i
                    
        return res
    
    def invalid_ids_2(self, ranges):
        res = 0
        
        for rg in ranges:
            start, end = self.get_range(rg)
            for i in range(start, end):
                if self.is_invalid_2(i):
                    res += i
                    
        return res
    
    def is_invalid_1(self, id: int) -> bool:
        id_string = str(id)
        n = len(id_string)
        
        
        if n % 2 != 0:
            return False
        
        n = n // 2
        
        return id_string[:n] == id_string[n:]
    
    
    def is_invalid_2(self, id: int) -> bool:
        s = str(id)
        n = len(s)
        
        for k in range(1, n // 2 + 1):
            if n % k != 0:
                continue
            
            block = s[:k]
            if block * (n // k) == s:
                return True
        
        return False

    
    def get_range(self, range: str):
        values = range.split('-')
        
        start = int(values[0])
        end = int(values[1])
        
        return [start, end + 1]
    
    
    def get_data(self, file_path: str):
        ranges = []
        
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    ranges += line.strip().split(',')
            return ranges
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        
