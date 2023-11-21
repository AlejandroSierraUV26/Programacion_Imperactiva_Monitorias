import numpy as np
from tabulate import tabulate

matrix1 = [
    [0, 0, 0], 
    [0, 0, 0],
    [0, 0, 0]
]

matrix1 = np.array(matrix1)

matrix1[0][0] = 1
matrix1[1][1] = 1
matrix1[2][2] = 1

print(tabulate(matrix1, tablefmt="fancy_grid", showindex="always", numalign="center", stralign="center", headers=["", "0", "1", "2"]))