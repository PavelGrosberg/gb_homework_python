cubes = [cube ** 3 for cube in range(1, 1001, 2)]
new_cubes = [cube for cube in cubes if sum(map(int, str(cube))) % 7 == 0]
cubes = [cube + 17 for cube in cubes]
cubes = [cube for cube in cubes if sum(map(int, str(cube))) % 7 == 0]
print(sum(new_cubes))
print(sum(cubes))
