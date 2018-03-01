import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN, KMeans
from sklearn import metrics

def distance(x, y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

def prep_data(rides):
    return np.array([ [r['start'][0], r['start'][1]] for r in rides ])

def compute_centers(data, labels):
    centers = {}
    for p, l in zip(data, labels):
         if l not in centers:
             centers[l] = {'avg':[0, 0], 'cnt':0}
         centers[l]['avg'] = centers[l]['avg']+p
         centers[l]['cnt'] = centers[l]['cnt']+1
    for k in centers:
        centers[k]['avg'] = centers[k]['avg']/centers[l]['cnt']
    return centers


def cluster_points_old(rides):
    data = prep_data(rides)
    labels = DBSCAN(eps=0.001, min_samples=10, metric=distance).fit_predict(data)
    centers = compute_centers(data, labels)
    return centers, labels

def cluster_points(rides, n_clusters):
    data = prep_data(rides)
    labels = KMeans(n_clusters=n_clusters).fit_predict(data)
    centers = compute_centers(data, labels)
    return centers, labels

def print_clusters(clusters):
    print("number of clusters: "+ str(len(centers)))
    print("centers are:")
    print([x['avg'] for x in clusters.values()])

if __name__ == "__main__":
    from read_ds import *
    rides = read_ds( 'c_no_hurry.in' )
    grouped_rides = {} 
    for r in rides:
        key = r['early_start']%1
        if key not in grouped_rides:
            grouped_rides[key] = []
        grouped_rides[r['early_start']%3].append(r)
    for start in grouped_rides:
        centers, labels = cluster_points(grouped_rides[start], 5)
        print_clusters(centers)
