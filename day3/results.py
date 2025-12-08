from day3 import Day3 


day = Day3()

# Part One
banks = day.get_data('data.txt')

res = day.sum_of_joltages_in_banks(banks)
# print(res)

# part two
res = day.sum_of_joltages_in_banks_2(banks)
print(res)