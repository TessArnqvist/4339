import pandas as pd
import numpy as np
import matplotlib as plt

"""
df = pd.DataFrame(
    {
        "Returns": ["Asset A", "Asset B"],  # Data for first column
        "State 1": [-0.02, 0.05],  # Data for second column
        "State 2": [-0.01, 0.03],  # and so on...
        "State 3": [0.03, -0.05],
    }
)

print(df.head())  # Display DataFrame first columns
"""

A = np.array([-0.02, -0.01, 0.03])
B = np.array([0.05, 0.03, -0.05])
sumA = A.sum() * 1 / 3
sumB = B.sum() * 1 / 3
print(sumB)


print(np.corrcoef(A, B))

print(A[0])
