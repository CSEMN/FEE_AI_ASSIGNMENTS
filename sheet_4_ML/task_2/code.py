import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from kneed import KneeLocator

# Importing the dataset
dataset = pd.read_csv('Wuzzuf_Jobs.csv')


#1. Factorize the YearsExp feature and convert it to numbers in new column.
dataset['YearsExpFact'] = pd.factorize(dataset['YearsExp'])[0]

#2. Apply K-means for job title and companies.
#dataset['TitleFact'] = pd.factorize(dataset['Title'])[0]
#dataset['CompanyFact'] = pd.factorize(dataset['Company'])[0]
X = dataset.iloc[:, [0, 1]].values
X = pd.DataFrame(X)
X = pd.get_dummies(X,columns=[0,1])

#pick best number of clusters
wcss = []
for i in range(1, 21):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

#graph method    
plt.plot(range(1, 21), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#mathmatical method    
k1 = KneeLocator(range(1, 21), wcss, curve="convex", direction="decreasing")
print("elbow at : ",end="")
print(k1.elbow)

# from graph & mathmatical methods best number of clusters = 2
#perform k-means algo
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)
y_kmeans == 0
