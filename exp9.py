import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.set() 
from sklearn.cluster import KMeans 
data = pd.read_csv('C:/Users/test/Desktop/Sathya/python programs/country.csv') 
data 
plt.scatter(data['Longitude'],data['Latitude']) 
plt.xlim(-180,180) 
plt.ylim(-90,90) 
plt.show() 
x = data.iloc[:,1:3] # 1t for rows and second for columns 
x 
kmeans = KMeans(3) 
kmeans.fit(x) 
identified_clusters = kmeans.fit_predict(x) 
identified_clusters 
kmeans.array([1, 1, 0, 0, 0, 2]) 
data_with_clusters = data.copy() 
data_with_clusters['Clusters'] = identified_clusters 
plt.scatter(data_with_clusters['Longitude'],data_with_clusters['Latitude'],c=data_with_clusters['Clusters'],cmap='rainbow')
