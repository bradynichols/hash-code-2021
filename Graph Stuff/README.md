# Graph Representation
Using pydot and graphviz, we create a graph cityplan representing intersections as nodes and streets as edges.
Then we create subsets of this graph detailing the path that each car goes through.

## TODO
- Create a "clock" to determine the time it takes for a car to complete its path.
- Create pointers representing the cars that dynamically change as the clock progresses.
- Determine when the cars are not able to pass through an intersection due to a red light
- Create the algorithm that would yield an optimized schedule. (Big)
