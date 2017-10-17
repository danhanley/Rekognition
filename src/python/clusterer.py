import os
import csv
import numpy
import matplotlib.pyplot as plt
import pylab as pl
import scipy as sp
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

NUM_CLUSTERS = 4

INPUT_FOLDER = "../../"
INPUT_FILE = "universe.csv"


def main():
    print("Loading universe")
    labels, ids, values = parse_file(INPUT_FOLDER, INPUT_FILE)
    kmeans = KMeans(n_clusters=NUM_CLUSTERS).fit(values)
    for i in range(len(ids)):
        print(ids[i], kmeans.labels_[i])

    pca = PCA(n_components=3).fit(values)
    pca_2d = pca.transform(values)
    pl.figure('Reference Plot')
    pl.scatter(pca_2d[:, 0], pca_2d[:, 1])
    kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=999)
    kmeans.fit(values)
    pl.figure('K-means with 3 clusters')
    pl.scatter(pca_2d[:, 0], pca_2d[:, 1], c=kmeans.labels_)
    pl.show()


def parse_file(dirname, filename):
    values = []
    labels = []
    ids =[]
    with open(os.path.join(dirname, filename), "r") as csvfile:
        reader = csv.reader(csvfile)
        header_skipped = False
        for row in reader: # each row is a list
            if (not header_skipped):
                labels = row[1:] #drop the "filename" title
                header_skipped = True
            else:
                ids.append(row[0])
                values.append(row[1:])
    csvfile.close()
    return labels, ids, numpy.asfarray(values,float) #cast strings to floats


if __name__ == "__main__":
    main()