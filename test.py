import mse
import numpy as np

a = np.zeros((3, 3))
b= np.zeros((3, 3))
for i in range(3):
    for j in range(3):
            a[i][j] = (i+1)*(j+1)
            if j%2 == 0:
                b[i][j] = a[i][j] +1
            else:
                b[i][j] = a[i][j] - 1

#print(a)
#print(b)
#mse.mse(a, b, 0)

mse.init_cmp("test_data_/7.jpg", "test_data_/3.jpg")
mse.init_cmp("test_data_/19.jpg", "test_data_/2.jpg")