import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics

def distance(x, y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

def cluster_points(rides):
    data = np.array([ [r['start'][0], r['start'][1]] for r in rides ])
    labels = DBSCAN(eps=0.3, min_samples=10, metric=distance).fit_predict(data)
    centers = {}
    for p, l in zip(data, labels):
        if l not in centers:
            centers[l] = {'avg':[0, 0], 'cnt':0}
        centers[l]['avg'] = (centers[l]['avg']+p)/(centers[l]['cnt']+1)
        centers[l]['cnt'] = centers[l]['cnt']+1
    return centers, labels


def print_clusters(clusters):
    print("number of clusters: "+ str(len(centers)))
    print("centers are:")
    print([x['avg'] for x in clusters.values()])

if __name__ == "__main__":
    from read_ds import *
    rides = read_ds( 'a_example.in' )
    centers, labels = cluster_points(rides)
    print_clusters(centers)
