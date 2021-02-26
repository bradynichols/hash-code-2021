import pydot
import os

def timetaken(carpath):
    time = 0
    for street in carpath.get_edge_list():
        time += int(street.get_attributes().get("len"))


if __name__ == '__main__':
    os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'
    # File input
    file = open("a.txt")
    list_of_lines = file.readlines()

    first_line = list_of_lines[0].split(" ")

    simulation_time = int(first_line[0])
    number_of_intersections = int(first_line[1])
    number_of_streets = int(first_line[2])
    number_of_cars = int(first_line[3])
    points = int(first_line[4])

    roads = []
    for line in list_of_lines[1:number_of_streets+1]:
        """strips the trailing whitespace """
        roads += [list(line.rstrip().split(" "))]
    print("######ROADS###########")
    print(roads)

    paths = []
    for line in list_of_lines[number_of_streets+1:]:
        """strips the trailing whitespace """
        paths += [list(line.rstrip().split(" "))]
    print("######PATHS###########")
    print(paths)
    file.close()

    # Graph Creation
    cityplan = pydot.Dot('cityplan', graph_type='graph', directed=True)

    # Add intersections
    for intersecindex in range(number_of_intersections):
        cityplan.add_node(pydot.Node(str(intersecindex)))

    # Add roads
    for road in roads:
        cityplan.add_edge(pydot.Edge(road[0], road[1], dir="forward", label=road[2], len=road[3]))

    # Output Graph to PNG(Optional)
    cityplan.write_png('cityplan.png')

    # Add paths
    paths_as_subgraphs = []
    for pathsindex in range(len(paths)):
        cursubgraph = pydot.Subgraph("Path " + str(pathsindex), directed=True, simplify=True)
        for streetindex in range(2,len(paths[pathsindex])):
            for road in cityplan.get_edge_list():
                if road.get_attributes().get("label") == paths[pathsindex][streetindex]:
                    cursubgraph.add_edge(road)
        for intersecindex in range(len(cursubgraph.get_edge_list())):
            cursubgraph.add_node(cityplan.get_node(cursubgraph.get_edge_list()[intersecindex].get_source())[0])
            if intersecindex == (len(cursubgraph.get_edge_list())-1):
                cursubgraph.add_node(cityplan.get_node(cursubgraph.get_edge_list()[intersecindex].get_destination())[0])
        cityplan.add_subgraph(cursubgraph)


    print(cityplan.get_subgraph_list()[0])

