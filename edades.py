# -*- coding: utf-8 -*-

def edades(edad):
	"""	
	Además de ser comentarios se pueden utilzar para hacer pruebas sencillas
	
	>>> edades(5)
	Eres niño

	>>> edades(-2)
	No existes

	>>> edades(17)
	Eres adolescente

	>>> edades(64)
	Eres adulto

	>>> edades(110)
	Eres adulto mayor

	>>> edades(140)
	Eres mumm-ra

	"""
	if edad<=0:
		print ("No existes")
	elif edad<= 13:
		print ("Eres niño")
	elif edad<=18:
		print ("Eres adolescente")
	elif edad<=65:
		print ("Eres adulto")
	elif edad<=120:
		print ("Eres adulto mayor")
	else:
		print ("Eres mumm-ra")

if __name__ == "__main__":
    import doctest
    doctest.testmod()