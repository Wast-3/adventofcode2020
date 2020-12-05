def evaluate(lowest, highest, letter, password):
    global valid_passwords
    lowflag = False
    highflag = False
    for i, char in enumerate(password):
        if i == lowest-1:
            if char == letter:
                lowflag = True
                print("Charachter at low position " + str(lowest-1) + " is " + char + " which is the same as target char " + letter)
        if i == highest-1:
            if char == letter:
                highflag = True
                print("Charachter at high position " + str(highest-1) + " is " + char + " which is the same as target char " + letter)
    if lowflag == True and highflag == True:
        return(False)
    if lowflag == True or highflag == True:
        return(True)

def parse_entry(entry):
    for i, char in enumerate(entry):
        if char == "-":
            lowest = int(entry[:i])
            lowest_index = i
        if char == " ":
            highest = int(entry[lowest_index+1:i])
            letter = entry[i+1]
            break
    return(lowest, highest, letter)

with open("challenge.txt") as challenge_text:
    valid_passwords = 0
    for line in challenge_text:
        line = line.strip()
        lowest, highest, letter = parse_entry(line)
        print(line)
        for i, char in enumerate(line):
            if char == ":":
                password = line[i+2:]
                result = evaluate(lowest, highest, letter, password)
                if result == True:
                    valid_passwords += 1
    print(str(valid_passwords)) 
