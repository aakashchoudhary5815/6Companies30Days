def atoi(self,string):
    # Code here
    c = 0
    for i in string:
        if i.isdigit() or i == '-' or i == '+':
            c += 1
    if c == len(string):
        return int(string)
    else:
        return -1