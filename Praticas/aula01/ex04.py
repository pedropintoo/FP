segundos = int(input("Segundos: "))
horas = (segundos // 3600) 
segundos = segundos - 3600*horas
minutos = segundos // 60
segundos = segundos - 60 * minutos



print(f"\n{horas:02} : {minutos:02} : {segundos:02}\n")