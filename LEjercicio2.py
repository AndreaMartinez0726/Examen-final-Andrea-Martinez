print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------- Ejercicio 2 ----------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
#Ejercicio2
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# Calcule la covarianza entre `u` y `v` e imprima su valor.

import numpy as np
import matplotlib.pylab as plt
u = np.array([12.,45.,6.,78.,34.,22.,-10.,31.,-27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])



cov=np.zeros(len(u),len(u))
n=len(u)
def cova(u,v):
	
	
	for i in range (len(u)):
		for j in range (len(v)):
			upro= u[i]-np.mean(u)
			vpro= v[j]-np.mean(v)
			cov[i]= np.sum( (upro*vpro)/n-1 )
			
	return cov
covarianza=cova(u,v)


print covarianza


