
def submit(schedules):
    
    # Cleaves any intersection without roads or roads with 0 time from schedules
    for intersection in schedules: 
        for x in range(len(intersection.keys())): # since we are changing the size of the dictionary, we need to do this
            for road in intersection.keys(): # removes roads with 0 seconds
                if intersection[road] == 0:
                    del intersection[road]
                    break
                
        if len(intersection) == 0: # removes intersections with 0 roads
            schedules.remove(intersection)

    # Prints the contents of schedules in the right format to submission.txt    
    submission = open("submission.txt","a")
    submission.truncate(0) # erases submissions
    submission.write(str(len(schedules)) + "\n") # writes number of intersections
    for intersection in schedules: 
        submission.write(str(schedules.index(intersection)) + "\n") # writes id of intersection
        submission.write(str(len(intersection)) + "\n") # writes number of roads in intersection
        for road in intersection.keys():
            submission.write(road + " " + str(intersection[road]) + "\n")
    submission.close()
