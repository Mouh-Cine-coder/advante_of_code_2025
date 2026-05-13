from day10 import Day10


day = Day10()

machines = day.get_data("data.txt")


# for m in machines:
#     print(m)


res = day.part_one(machines)
print(res)
