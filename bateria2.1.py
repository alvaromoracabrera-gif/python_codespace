segundos = int(input("segundos: "))

dias = segundos // 86400
sobrante = segundos % 86400
horas = sobrante // 3600
sobrante = sobrante % 3600
minutos = sobrante // 60
resto = sobrante % 60

print(f"{segundos} segundos son {dias} dias, {horas} horas, {minutos} minutos y {resto} segundos")
