import numpy as np
import os
import sys

#os.system('cls')
I = np.array([83,98,100],dtype='float')
z_ass = 500
z_calc = 0
k = 738420
alpha = 100
beta = 100
i = 0
arr = list(map(float, input('Enter I1, I2 and I3\n').split()))
try:
	I = arr
except:
	print('Invalid input')
	sys.exit()
	
while(abs(z_ass-z_calc) > 0.1):
	z_ass = 0.5*(z_ass+z_calc)
	r1 = pow(((k*z_ass)/I[0]),1/3)
	r2 = pow(((k*z_ass)/I[1]),1/3)
	r3 = pow(((k*z_ass)/I[2]),1/3)
	y  = (r1*r1-r3*r3+beta*beta)/(2*beta)
	x  = (r1*r1-r2*r2+alpha*alpha)/(2*alpha)
	print('x = ',round(x,2),'y = ',round(y,2),'z = ',round(z_calc,2),'r1 = ',round(r1,2),'r2 = ',round(r2,2),'r3 = ',round(r3,2))
	if((r1*r1-(x*x+y*y))<0):
		z_calc = 0.5*z_ass
	else:
		z_calc = np.sqrt((r1*r1-(x*x+y*y)))#+np.sqrt((r2*r2-((x-alpha)*(x-alpha)+y*y)))+np.sqrt((r3*r3-(x*x+(y-beta)*(y-beta)))))/3
	#print('z_calc = ',round(z_calc,2),'z_ass = ',round(z_ass,2))
	i = i+1
	if(i == 1000):
		break
if(i == 1000):
	print('no convergence :(')
else:
	print('x = ',round(x,2),'y = ',round(y,2),'z = ',round(z_calc,2), 'iterations = ',i)

		


