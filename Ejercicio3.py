# -*- coding: utf-8 -*- 


def final(exa1,exa2,exa3):

	"""
	>>> final(7,6,9)
	7
	"""


	suma = exa1 + exa2 + exa3
	final = suma/3
	
	print final




if __name__=="__main__":
	import doctest
	doctest.testmod()