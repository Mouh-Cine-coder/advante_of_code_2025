from day2 import Day2


day = Day2()

ranges = []
ranges = day.get_data('data.txt')
# ****************** PART ONE ******************
res = day.invalid_ids_1(ranges)
print(res)

# **********************************************

# ****************** PART TWO ******************
res = day.invalid_ids_2(ranges)
print(res)
# **********************************************


