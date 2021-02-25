from read_problem import simulation_time, number_of_intersections, number_of_streets, number_of_cars, points_per_car

from read_problem import roads, paths

from main import intersections

roads_and_their_intersections = {}
for intersection in range(len(intersections)):
    for road in intersections[intersection]:
        roads_and_their_intersections[road] = intersection

# print("simtime " + str(simulation_time))
# print("intersections " + str(number_of_intersections))
# print("streets " + str(number_of_streets))
# print("cars " + str(number_of_cars))
# print("points " + str(points_per_car))

# print(intersections)

# print(roads)
# print(paths)

class Simulation:
    def __init__(self, schedule):

        self.cars = []
        for x in range(number_of_cars):
            self.cars.append(Car(paths[x]))
        
        self.schedule = schedule # track schedule for lights
        self.intersections_onoff = schedule # track if intersections are on or off

        #modifying schedule
        self.intersection_schedules = [] #list of lists for pass_one_second
        for intersection in schedule:
            temp_list = []
            for road in intersection.keys():
                for x in range(0, intersection[road]):
                    temp_list.append(road)
            temp_list *= simulation_time # preserves the pattern, is too big but that doesn't matter
            temp_list = temp_list[0:simulation_time]
            self.intersection_schedules.append(temp_list)


            
# i want to turn [a, a, b] into [a, a, b, a, a, b...] where the second list has a len equal to
# the total time the simulation will run for

        for intersection in self.schedule:
            for road in intersection.keys():
                intersection[road] = 0 # all intersections red at start

        self.secondspassed = 0

    def pass_one_second(self):
        # first update intersections
        for intersection in range(number_of_intersections-1):
            # check schedule, then update intersections_onoff
            current_green_light = self.intersection_schedules[intersection][self.secondspassed]
            for road in self.intersections_onoff[intersection]:
                if road == current_green_light:
                    self.intersections_onoff[intersection][road] = 1
                else:
                    self.intersections_onoff[intersection][road] = 0

        # check each car and move it
        for car in cars:
            nextroad = path[current_position]
            # find if next road is green
            if self.intersections_onoff[self.intersection[nextroad]] == 1:
                self.position_along_path += 1
                self.nextroad = 


        self.secondspassed += 1


class Car:
    # path: path
    # roads_in_path: amount of roads in path
    # reached: boolean if reached
    # time_reached: 0 if not reached, else time reached
    def __init__(self, path):
        self.path = path[1:]
        self.roads_in_path = path[1]
        self.reached = False
        self.time_reached = 0
        self.position_along_path = 0
        # for this, we need a way to translate the car's starting road to the intersection
        # so that when we are updating the car's position, we know where to access 
        self.intersection = roads_and_their_intersections[self.path[0]]



sim = Simulation(intersections)

# print(sim.cars[0].path)
print(sim.intersections_onoff)
sim.pass_one_second()
print(sim.intersections_onoff)
sim.pass_one_second()
print(sim.intersections_onoff)
sim.pass_one_second()
print(sim.intersections_onoff)
sim.pass_one_second()
print(sim.intersections_onoff)


# testcar = Car('yeet')