# -*- coding: utf-8 -*- 


def tienda(com1,com2,com3):


	"""
	>>> tienda(100,59,23)
	27.3
	154.7
	"""	
	
	suma = com1 + com2 + com3
	descuento= suma * 0.15
	total = suma - descuento
	
	print descuento
	print total


if __name__=="__main__":
	import doctest
	doctest.testmod()