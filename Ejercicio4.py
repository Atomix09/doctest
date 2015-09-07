# -*- coding: utf-8 -*- 


def porcentaje(alumnos,hombres,mujeres):

	"""
	>>> porcentaje(20,5,15)
	25
	75
	"""
        porcentaje1= (hombres*100)/alumnos
        porcentaje2 = (mujeres*100)/alumnos

	print porcentaje1
	print porcentaje2


if __name__=="__main__":
	import doctest
	doctest.testmod()