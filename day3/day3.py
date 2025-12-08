class Day3:
    
    def sum_of_joltages_in_banks(self, banks):
        joltages = 0
        
        for bk in banks:
            joltages += self.best_joltage_in_a_bank(bk)
        
        return joltages
    
    def sum_of_joltages_in_banks_2(self, banks):
        joltages = 0
        
        for bk in banks:
            joltages += self.best_joltage_with_12_digits_in_a_bank(bk)
        
        return joltages
    
    def best_joltage_in_a_bank(self, bank):
        
        res = 0
        # i feel like this is horrible and i cheated by getting an answer with an 0(n^2) TC solution but i will optimize it later
        for i in range(len(bank)):
            for j in range(i+1,len(bank)):
                num = int(bank[i]) * 10 + int(bank[j])
                res = max(res, num)
        
        return res
    
    
    def best_joltage_with_12_digits_in_a_bank(self, bank):
        remove = len(bank) - 12
        stack = []    
        for dg in bank:
            while stack and remove > 0 and int(stack[-1]) < int(dg):
                stack.pop()
                remove -= 1
            stack.append(dg)
        
        return int(''.join(stack[:12]))
    
        
        
        
    def get_data(self, file_path: str):
        banks = []
        
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    banks.append(line.strip())
                    
            return banks
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
