# FROM PROBLEM
problem_file = open("a.txt")
list_of_lines = problem_file.readlines()

first_line = list_of_lines[0].split(" ")

simulation_time = int(first_line[0])
number_of_intersections = int(first_line[1])
number_of_streets = int(first_line[2])
number_of_cars = int(first_line[3])
points_per_car = int(first_line[4])


roads = []
for line in list_of_lines[1:number_of_streets+1]:
    """strips the trailing whitespace """
    roads += [list(line.rstrip().split(" "))]
# print("######ROADS###########")
# print(roads)

paths = []
for line in list_of_lines[number_of_streets+1:]:
    """strips the trailing whitespace """
    paths += [list(line.rstrip().split(" "))]
# print("######PATHS###########")
# print(paths)
problem_file.close()
