def sim_sled(lines, xvector, yvector):
    xpos = 0
    ypos = 0
    collisions = 0
    bottom = len(lines)-1
    while ypos <= bottom:
        line = lines[ypos]
        line = line.strip()
        char = line[xpos]
        if char == "#":
            print("sled will collide with tree at position: " + str(xpos) + " " + str(ypos))
            collisions += 1
        ypos += yvector
        xpos += xvector
        if xpos >= len(line):
            xpos = xpos - len(line)
    return(collisions)

with open("challenge.txt") as challenge_text:
    route_results = []
    answer = 1
    lines = challenge_text.readlines()
    test_routes = ((1,1), (3,1), (5,1), (7,1),(1,2))
    for i in test_routes:
        xvector = i[0]
        yvector = i[1]
        print("testing route " + str(i))
        route_results.append(sim_sled(lines, xvector, yvector))
        answer *= sim_sled(lines, xvector, yvector)
    print(str(route_results))
    print(answer)
