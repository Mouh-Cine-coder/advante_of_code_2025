from day5 import Day5


day = Day5()

ranges = day.get_ranges('data/ranges.txt')

ids = day.get_ids('data/ids.txt')

rr = day.reduce_ranges(ranges)

res_part_1 = day.count_fresh_products(rr, ids)
res_part_2 = day.count_fresh_ids(rr)

print(res_part_1)

