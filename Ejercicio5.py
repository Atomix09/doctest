# -*- coding: utf-8 -*- 


def unidad(pesos,dolar):

	"""
	>>> unidad(200,17)
	3400
	200
	"""
        pesos = pesos * dolar
        dolares = pesos/17
	
	print pesos
	print dolares



if __name__=="__main__":
	import doctest
	doctest.testmod()