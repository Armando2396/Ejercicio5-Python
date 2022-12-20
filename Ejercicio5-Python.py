def es_bisiesto(año):
	return not año % 4 and (año % 100 or not año % 400)


for año in range(1996, 2022):
	if es_bisiesto(año):
		print(año, end=' ')