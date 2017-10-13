import os
import csv
import numpy
import matplotlib.pyplot as plt
from sklearn import svm

INPUT_FOLDER = "../../"
INPUT_FILE = "universe.csv"


def main():
    print("Loading universe")
    labels, ids, values = parse_file(INPUT_FOLDER, INPUT_FILE)


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