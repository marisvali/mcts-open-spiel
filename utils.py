def write_to_csv(vals, create: bool):
    if create:
        f = open("vals.csv", "w")
    else: 
        f = open("vals.csv", "a")
    line = ''
    for i in range(len(vals) - 1):
        line += str(vals[i]) + ','
    line += str(vals[-1]) + '\n'
    f.write(line)