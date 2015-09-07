# -*- coding: utf-8 -*- 


def unidad(pesos,dolar):

	"""
	>>> unidad(20,17)
	340
	"""
        conversion = pesos * dolar

	print conversion



if __name__=="__main__":
	import doctest
	doctest.testmod()