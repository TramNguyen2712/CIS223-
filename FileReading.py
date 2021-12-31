# We want to process the data from earthquakes.txt such that
# 1. Extract the magnitudes data into an appropriate data structure
# 2. Calculate the average of all magnitudes, and the standard deviation
# 3. plot a histogram of the distribution of magnitudes
#   3.1 Include the mean and the standard deviation of the distribution of the data

import numpy as np
import matplotlib.pyplot as plt

fileName = "earthquakes.txt"

def magnitudesListMaker(file):
    magnitudes = []
    inputFileStream = open(file, mode='r')  # open as read-only

    inputFileStream.readline()   # reads one line and moves on to the next line

    for line in inputFileStream:
        lineItems = line.split()     # split() returns a list of string objects from a line separated by the input
        magnitudes.append(float(lineItems[0]))  # recall a list is indexed with numbers starting at 0

    inputFileStream.close()
    return magnitudes

mags = magnitudesListMaker(fileName)
print(len(mags), mags)



mean = round(np.mean(mags), 2)
std = round(np.std(mags), 2)
print(mean, std)


# Plot magnitude data

# to draw a histogram we need a num_bins
num_bins = 50
n, bins, patches = plt.hist(mags, num_bins, facecolor='green')

# add labels
plt.xlabel("Magnitude")
plt.ylabel("Count")
plt.title("Histogram of Earthquakes magnitudes")

# add lines (vertical) that identify the mean and the standard deviation
plt.axvline(mean, color='blue', linestyle='dashed', linewidth=2)
plt.axvline(mean + std, color='red', linestyle='dashed', linewidth=1)
plt.axvline(mean - std, color='red', linestyle='dashed', linewidth=1)


plt.show()


