from math import sqrt
from union_find import UnionFind
from collections import Counter


class Day8:
    
    
    """
        In order to solve this problem i found out that learning about Union find would help alot (comments from reddit)
        This video helps visualze it and implemeting it as well as optimizing it by using Rank size and path compression: https://www.youtube.com/watch?v=92UpvDXc8fs
    """
    
        
    def list_points_distances(self, coordinates):
        n = len(coordinates)
        
        res = []
        for i in range(n):
            p1 = coordinates[i][0], coordinates[i][1], coordinates[i][2]
            for j in range(i + 1, n):
                p2 = coordinates[j][0], coordinates[j][1], coordinates[j][2]
                dist = self.distance(p1, p2)
                res.append((dist, i, j))
        
        # I return the list (distance, p1, p2) sorted by distance meaning the points are going to be near each other
        return sorted(res, key=lambda pairs: pairs[0])
    
    
    def first_1000_jbs(self, distances):
        
        """
            chwiya diyal 3ya9a here o arithmetic series z3ma bch nbyn lrasi lmath lidrt f bac ra nf3i chihaja
            i could just pass the lenth of the coordinates in the params but let do some show offs with math 
            
            Here i need the len of the junction boxes before calculating the distances
            but we know that the distances are calculated for each number with the rest of the numbers 
            
            if the original len of the coordinates is 3 then the number of the distances is 3 + 2 + 1 = 6
            aaaaaand what is this my friend, it is just a sum of an arithmetic series n * (n + 1)  / 2 from n to 1
            
            so let number_distances = number_coordinates * (number_coordinates + 1 ) // 2
            but what we have here is number_distances and we want number_coordinates
            then we have to solve :
                number_coordinates is x for simplicity 
                number_distances is y (think of this as a known)
                x^2 + x - 2y = 0
                
                two solution but taking the positive one only here
                x = (-1 + sqrt(1 + 8y)) // 2
                
            
        """
        
        y = len(distances)
        
        n = int((-1 + sqrt(1 + 8 * y)) // 2) + 1
        
        uf = UnionFind(n)
        
        
        for index in range(1000):
            _, i, j = distances[index]
            uf.union(i, j)
        
        sizes = Counter(uf.find(i) for i in range(n))
        
        print(sizes)
        
        largest = sorted(sizes.values(), reverse=True)
        res = largest[0] * largest[1] * largest[2]
        
        return res
    
    
    def distance_between_wall_jb(self, coodinates, ditances):
        n = len(coodinates)
        
        
        components = n
        uf = UnionFind(n)
        
        for _, i, j in ditances:
            if uf.union(i, j):       
                components -= 1

                if components == 1:
                    print("p1 ===> ", coodinates[i])
                    print("p2 ===> ", coodinates[j])
                    x1 = coodinates[i][0]
                    x2 = coodinates[j][0]
                    return x1 * x2
                
        return -1
            
        
        
                
    
    def distance(self, p1, p2):
        x1, y1 , z1 = p1
        x2, y2 , z2 = p2
        
        return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2))
        
    
    
    def get_data(self, file_path):
        coordinates = []
        try:
            with open(file_path, 'r') as file:
                coordinates = [tuple(map(int, line.strip().split(','))) for line in file]
            
            return coordinates
        except FileNotFoundError as e:
            print("error occured: ", e)