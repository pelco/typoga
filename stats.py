#!/bin/env python
import os
import sys
import matplotlib.pyplot as plt
import numpy as np


def parse_file(pfile,pos):
    """
    """
    # Check if file exists
    if not os.path.exists(pfile):
        print("File %s does not exist" % pfile)
        return

    hsf = open(pfile,"r")

    lines = hsf.readlines()
    lines = lines[3:] # skip header

    scores=[]
    # Read every line
    for line in lines:
        #print line
        line = line.strip() # remove \n
        line = line.split(":")

        scores.append(float(line[1])) # store only highscores

    if len(scores) == 0:
        print("You should have at least 1 highscores for %s" % pfile)
        return

    # Calculate mean value before appending 0 value at the end
    mean = np.mean(scores)
    # Append zero to get space to print mean value
    scores.append(0)

    x = np.arange(1,len(scores)+1)

    plt.subplot(3, 1, pos)
    plt.ylabel('HighScores')
    plt.title(pfile)

    # Draw bar plot
    plt.bar(x, scores)
    # Draw orange bar for the highest value
    max_val = np.argmax(scores)
    plt.bar(max_val+1, scores[max_val], color='orange')
    plt.text(max_val+1, scores[max_val], ("%.02f" % scores[max_val]), fontsize=10, color='black')

    # Draw mean line
    mean_line = plt.plot([0, len(scores)], [mean, mean], 'r')
    plt.text(len(scores), mean, ("%.02f" % mean), fontsize=10, color='red')

def main():
    """
    """
    parse_file("scores/highScore_random.txt", 1)
    parse_file("scores/highScore_phrases.txt", 2)
    parse_file("scores/highScore_programming.txt", 3)
    plt.xlabel('N Games')
    plt.show()

if __name__ == '__main__':
    main()