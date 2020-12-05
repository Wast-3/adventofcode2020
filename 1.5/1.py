expense_report_list = []

with open("challenge.txt") as challenge_text:
    for line in challenge_text:
        line = line.strip()
        try:
            line = int(line)
        except:
            continue
        expense_report_list.append(line)

for i in expense_report_list:
    for j in expense_report_list:
        if (i + j) == 2020:
            print(i * j)

