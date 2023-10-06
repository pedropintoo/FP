def allMatches(Teams):
    Matches = []
    for i in Teams:
        for p in range(len(Teams)):
            if i != Teams[p]: Matches.append((i,Teams[p]))
    return Matches

    
Equipas = ["SLB","FCP","BRG","PSG","RMD"]
print(allMatches(Equipas))