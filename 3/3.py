def sim_sled(text, xvector, yvector):
    xpos = 0
    ypos = 0
    collisions = 0
    lines = text.readlines()
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
    collisions = sim_sled(challenge_text, 3, 1)
    print(collisions)
    
