class Day5:
    
    
    def count_fresh_products(self, ranges, ids):
        fresh = 0
        
        for id in ids:
            for r in ranges:
                if id >= r[0] and id <= r[1]:
                    fresh += 1
                    break
    
                    
        return fresh 
    
    def count_fresh_ids(self, ranges):
        count = 0
        
        
        for r in ranges:
            count += r[1] - r[0] + 1
        
        return count
    
    def reduce_ranges(self, ranges):
        reduced_ranges = []
        ranges.sort(key=lambda x: x[0])

        for interval in ranges:
            if not reduced_ranges or reduced_ranges[-1][1] < interval[0]:
                reduced_ranges.append(interval)
            else:
                reduced_ranges[-1][1] = max(reduced_ranges[-1][1], interval[1])
        
        return reduced_ranges
            
            
    
    
    def get_ranges(self, file_path):
        ranges = []
        res = []
        
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    ranges.append(line.strip())
            
            for el in ranges:
                # split the elements and convert them to ints then add them to the res
                res.append(
                    list(
                        map(int, el.split('-'))
                    )
                )
            
            return res
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    
    def get_ids(self, file_path):
        ids = []
        
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    ids.append(int(line.strip()))
            
            return ids
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")