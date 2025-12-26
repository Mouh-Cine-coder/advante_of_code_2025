from day8 import Day8 


day = Day8()

data = day.get_data('data.txt')


# print(data[0])

distances = day.list_points_distances(data)

# print("length of distances", len(distances))


# res = day.first_1000_jbs(distances)


# print(res)

res = day.distance_between_wall_jb(data, distances)
print(res)
