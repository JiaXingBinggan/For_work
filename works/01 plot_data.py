import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据集
df = pd.read_csv('automobile.csv')

# 查看数据集信息
print(df.info())

# 查看数据集统计信息
print(df.describe())

# 检查缺失值
print(df.isnull().sum())
