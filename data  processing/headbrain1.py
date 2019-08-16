import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data1=pd.read_csv('headbrain.csv')
a=data1["Head Size(cm^3)"].values
b=data1.iloc[:,3].values