import math


cat1 = float(input("Medida do 1 cateto: "))
cat2 = float(input("Medida do 2 cateto: "))

hip = math.sqrt((cat1**2 + cat2**2))
hip2 = math.hypot(cat1,cat2)
print(hip2)
angulo = math.degrees(math.acos(cat1/hip))

print(f"\nHipotenusa: {hip:.2f}\nAngulo entre 1cateto e hipotenusa: {angulo:.2f}º\n")