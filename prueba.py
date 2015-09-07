# -*- coding: utf-8 -*- 

def edad(edades):
	
	"""
	
	>>> edad(-2)
	NO EXISTES
	
	>>> edad(11)
	Eres Nino
	
	>>> edad(15)
	Eres adolecente
	
	>>> edad(45)
	Eres Adulto :v
	
	>>> edad(78)
	Eres Adulto mayor
	"""
	
	if(edades <= 0):
		print "NO EXISTES"
	elif (edades <= 13):
		print "Eres Nino"
	elif(edades <= 18):
		print "Eres adolecente"
	elif (edades <= 65):
		print "Eres Adulto :v"
	elif(edades <= 120):
		print "Eres Adulto mayor"
	else:
		print "Eres Mumm-Ra D:"

if __name__=="__main__":
	import doctest
	doctest.testmod()