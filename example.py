import numpy as np

rows = 1000
cols = 1000
a = np.arange(rows*cols).reshape(rows, cols)

totalSum = 0
rowSum = np.zeros(rows, dtype=np.int32)

for i in range(rows):
    for j in range(cols):
        rowSum[i] += a[i][j]
        totalSum += a[i][j]

print(totalSum)
print(rowSum)
