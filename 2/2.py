counter = 0

def evaluate(lowest, highest, letter, password):
    global valid_passwords
    number_of_target_chars = 0
    for i, char in enumerate(password):
        if char == letter:
            number_of_target_chars += 1
    if number_of_target_chars <= highest and number_of_target_chars >= lowest:
        valid_passwords = valid_passwords + 1
    

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

global valid_passwords
valid_passwords = 0

with open("challenge.txt") as challenge_text:
    for line in challenge_text:
        counter = counter + 1
        line = line.strip()
        lowest, highest, letter = parse_entry(line)
        print(line)
        print("Lowest number is " + str(lowest) + " highest number is " + str(highest) + " letter is " + str(letter))
        print("\n")
        for i, char in enumerate(line):
            if char == ":":
                password = line[i+2:]
                evaluate(lowest, highest, letter, password)
    print(str(valid_passwords)) 
