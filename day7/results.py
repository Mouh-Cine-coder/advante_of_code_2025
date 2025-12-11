from day7 import Day7



day = Day7()


data = day.get_data('data.txt')

# beams = day.build_grid_beam(data)
# # for b in beams:
# #     print(''.join(b))

# splits = day.count_splits(beams)

# print(splits)


part2 = day.count_multitimes(data)
print(part2)