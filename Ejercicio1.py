# -*- coding: utf-8 -*- 


def tienda(ven1,ven2,ven3,base):


	"""
	>>> tienda(100,59,23,150)
	18.2
	168.2
	"""	
	
	comision1= ven1 * 0.10 
	comision2= ven2 * 0.10
	comision3 = ven3 * 0.10
	suma = comision1 + comision2 + comision3
	suma2 = suma + 150
	
	print suma
	print suma2


if __name__=="__main__":
	import doctest
	doctest.testmod()