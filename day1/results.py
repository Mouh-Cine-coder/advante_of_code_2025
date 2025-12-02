from day1 import Day1


day1 = Day1()

data = []
data = day1.get_data('data.txt')

# ****************** PART ONE ******************
res = day1.dial_at_zero_1(data)
print(res)
# **********************************************

# ****************** PART TWO ******************
res = day1.dial_at_zero_2(data)
print(res)
# **********************************************


