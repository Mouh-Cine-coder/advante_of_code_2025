class Day9:
    '''
        
    '''
    
    def largest_area(self, points):
        largest_area = float('-inf')
        
        for i in range(len(points)):
            col1, row1 = points[i]
            for j in range(1, len(points)):
                col2, row2 = points[j]
                area = (abs(int(row1) - int(row2) + 1)) * (abs(int(col1) - int(col2) + 1))
                # print(f'p1{points[i]} and p2{points[j]} and area {area}')
                largest_area = max(largest_area, area)
        
        return largest_area
    
    
    def get_data(self, file_path):
        data = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    data.append(tuple(line.strip().split(',')))
                
            return data
        except FileNotFoundError as e:
            print("File not found : ", e)