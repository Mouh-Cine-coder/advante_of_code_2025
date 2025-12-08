from day4 import Day4 


day = Day4()

lines = day.get_data('data.txt')



curr_grid, count = day.remove_until_done(lines)

print(count)





