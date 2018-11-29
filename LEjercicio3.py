print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------- Ejercicio 3 ----------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
#Ejercicio3
# Este codigo debe permitir hacer una estimacion bayesiana de parametros. Los datos CircuitoRC.txt tienen los datos de la carga de un condensador en un circuito RC. Su codigo debe estimar los parametros de R y C que resulten en el mejor ajuste de sus datos. 
# 1) IMPRIMA los mejores de valores de R y C encontrados
# 2) GRAFIQUE los datos originales y su ajuste. Guarde la grafica SIN MOSTRARLA en Ajuste.pdf. 

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = np.loadtxt('CircuitoRC.txt')

x_data=data[:,0]
y_data=data[:,1]

Rguess= 11.0
Cguess= 20.0

R_walk = np.empty((0))
C_walk = np.empty((0))
l_walk = np.empty((0))

R_walk = np.append(R_walk, Rguess)
C_walk = np.append(C_walk, Cguess)

def modelo(x_data,R,C):
	fun= (10.0*C)*(1-np.exp(-t_data/(R*C)))
	chi_squared = 0.5*sum((y_obs-y_model)**2)/len(x_data)
	l=np.exp(-0.5*chi)
	return l

#def modelo(t_data, R, C):
#    return (10.0*C)*(1-np.exp(-t_data/(R*C)))

#def likelihood(y_obs, y_model):
#    chi_squared = 0.5*sum((y_obs-y_model)**2)/len(x_data)
#    return np.exp(-chi_squared)




n_iterations = 20000

for i in range (n):
	cnuevo=random.normal(C_walk[i],0.1)
	rnuevo=random.normal(R_walk[i],0.1)
	alpha= modelo(x_data,rnuevo,cnuevo)/modelo(x_data,Rprueba[i],Cprueba[i])
	if(alpha>1):
		C_walk=np.append(C_walk,cnuevo)
		R_walk=np.append(R_walk,rnuevo)
		l_walk=np.append(l_walk,modelo(x_data,cnuevo,rnuevo))
	if (alpha<1):
		beta=random.random
		if (beta<alpha):
			C_walk=np.append(C_walk,cnuevo)
			R_walk=np.append(R_walk,rnuevo)
			l_walk=np.append(l_walk,modelo(x_data,cnuevo,rnuevo))
		if(beta>alpha)
			C_walk=np.append(C_walk,C_walk[i])
			R_walk=np.append(R_walk,R_walk[i])
			l_walk=np.append(l_walk,x_data,C_walk[i],R_walk[i]))
			
		
	 



# Complete el codigo (puede reescribir lo anterior si prefiere que su codigo tenga otra estructura)
# 1) IMPRIMA los mejores de valores de R y C encontrados
# 2) GRAFIQUE los datos originales y su ajuste. Guarde la grafica SIN MOSTRARLA en Ajuste.pdf. 
