import numpy as np
from matplotlib import pyplot as plt
import chanelsinterpolation
import pandas as pd
import time

linear_model = pd.read_csv("LinearRegression.csv", header=None)
linear_model = linear_model.as_matrix()
linear_model = linear_model.tolist()


samV = pd.read_csv("SamV.csv", header=None)
samV = samV.as_matrix()
samV = samV.tolist()

cpp_start = time.process_time()

answer = chanelsinterpolation.interpolate(samV, linear_model)

cpp_end = time.process_time()

print(cpp_end - cpp_start)