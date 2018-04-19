with open('hightemp.txt') as f:
    print((f.read()).replace("\t"," "), end='')

# sed $'s/\t/ /g' hightemp.txt
