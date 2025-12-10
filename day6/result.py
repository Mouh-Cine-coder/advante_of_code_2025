from day6 import Day6


day = Day6()

# ops, nums = day.get_data('data.txt')

# res = day.solve_math(ops, nums)
# print(res)

# Part Two

ops, raw_data = day.get_data_2('data.txt')
# print(ops)

    
gn = day.gather_numbers(raw_data)
# print(gn)
numbers = day.group_numbers(gn)
# print(numbers)


res = day.calculate_2(ops, numbers)
print(res)