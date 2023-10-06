import math

def play(times=3):
    global score

    score = 0
    while times > 0:
        times -= 1
        print("\n")
        print("Enter the coordinates in mm from the center of the board.")
        x = float(input("x? "))
        y = float(input("y? "))
        distance(x,y)
    print("\n")
    print('PONTUAÇÂO TOTAL: ',score)

def distance(x,y):
    global score

    if x!= 0 or y!= 0:
        distancexy = (math.sqrt(((x)**2) + ((y)**2)))
        if  distancexy > 170:
            score += 0
            print('Lançaste para fora! A tua pontuação é ',score)
        elif distancexy > 162:
            score += 2 * ponto(x,y,distancexy)
            print('Duplo! A tua pontuação é ',score)
        elif distancexy > 107:
            score += ponto(x,y,distancexy)
            print('Acertas-te! A tua pontuação é ',score)
        elif distancexy > 99:
            score += 3 * ponto(x,y,distancexy)
            print('Triplo! A tua pontuação é ',score)
        elif distancexy > 32:
            score += ponto(x,y,distancexy)
            print('Acertas-te! A tua pontuação é ',score)
        elif distancexy > 13:
            score += 25
            print('Acertas-te quase no centro! A tua pontuação é ',score)
        else:
            score += 50
            print('Acertas-te no centro! A tua pontuação é ',score)
    else: 
        score += 50
        print('Acertas-te no centro! A tua pontuação é ',score)
        
def ponto(x,y,distancexy):
    if y > 0:
        if -9 < math.degrees(math.asin((y/distancexy))) < 9:
            if x > 0: return 6
            else: return 11
        elif -9+(1*18) < math.degrees(math.asin((y/distancexy))) < 9+(1*18):
            if x > 0: return 13
            else: return 14
        elif -9+(2*18) < math.degrees(math.asin((y/distancexy))) < 9+(2*18):
            if x > 0: return 4
            else: return 9
        elif -9+(3*18) < math.degrees(math.asin((y/distancexy))) < 9+(3*18):
            if x > 0: return 18
            else: return 12
        elif -9+(4*18) < math.degrees(math.asin((y/distancexy))) < 9+(4*18):
            if x > 0: return 1
            else: return 5
        elif -9+(5*18) < math.degrees(math.asin((y/distancexy))) < 9+(5*18):
            return 20
    else:
        if -9 < math.degrees(math.asin((-y/distancexy))) < 9:
            if x > 0: return 6
            else: return 11
        elif -9+(1*18) < math.degrees(math.asin((-y/distancexy))) < 9+(1*18):
            if x > 0: return 10
            else: return 8
        elif -9+(2*18) < math.degrees(math.asin((-y/distancexy))) < 9+(2*18):
            if x > 0: return 15
            else: return 16
        elif -9+(3*18) < math.degrees(math.asin((-y/distancexy))) < 9+(3*18):
            if x > 0: return 2
            else: return 7
        elif -9+(4*18) < math.degrees(math.asin((-y/distancexy))) < 9+(4*18):
            if x > 0: return 17
            else: return 19
        elif -9+(5*18) < math.degrees(math.asin((-y/distancexy))) < 9+(5*18):
            return 3

play(2)