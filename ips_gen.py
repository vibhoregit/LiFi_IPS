import numpy as np
import os

os.system('cls')
I = np.array([83,98,100],dtype='uint16')
k = 738420
alpha = 100
beta = 100
i = 0

arr = list(map(float, input('Enter x, y, z, alpha and beta \n').split()))
x = arr[0]
y = arr[1]
z = arr[2]
alpha = arr[3]
beta = arr[4]
I[0] = (k*z/pow(np.sqrt(x*x+y*y+z*z),3))
I[1] = (k*z/pow(np.sqrt((x-alpha)*(x-alpha)+y*y+z*z),3))
I[2] = (k*z/pow(np.sqrt(x*x+(y-beta)*(y-beta)+z*z),3))

print('I1 = ', I[0],'I2 = ',I[1],'I3 = ',I[2])

