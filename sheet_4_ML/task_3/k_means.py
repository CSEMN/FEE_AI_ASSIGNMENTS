import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from kneed import KneeLocator

# Importing the dataset
dataset = pd.read_csv('diabetes.csv')

X = dataset.iloc[:, 0:8].values
X = pd.DataFrame(X)

#pick best number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

#graph method    
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
#mathmatical method    
k1 = KneeLocator(range(1, 11), wcss, curve="convex", direction="decreasing")
plt.scatter(k1.elbow,k1.elbow_y,label="Elbow point",c='r')
plt.legend()
plt.show()
print("elbow at : ",end="")
print(k1.elbow)

# from graph & mathmatical methods best number of clusters = 3
#perform k-means algo
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)