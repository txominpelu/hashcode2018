import matplotlib.pyplot as plt
import numpy
import scipy.cluster.hierarchy as hcluster

# generate 3 clusters of each around 100 points and one orphan point
def cluster_points(rides):
    data = [ [r['start'][0], r['start'][1]] for r in rides ]
    
    # clustering
    thresh = 1.5
    clusters = hcluster.fclusterdata(data, thresh, criterion="distance")

    # plotting
    return clusters


def print_clusters(clusters):
    title = "number of clusters: %d" % (len(set(clusters)))
    print(clusters)
