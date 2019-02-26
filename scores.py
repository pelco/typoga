#!/usr/bin/env python
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

WINDOW_TITLE = "Game Options"

# Game Options
RANDOM = "Random"
PH_LEADERS = "Leaders"
PROGRAMMING = "Programming"

GameOptions = [
    RANDOM,
    PH_LEADERS,
    PROGRAMMING ]

# The order must match exactly how scores are saved in the highscore file
SocreOptions = [
    "Scores",
    "Accuracy",
    "Words per minute",
    "Chars per minute",
    "Number of Words",
    "Number of Hit Chars",
    "Number of Missed Chars",
    "Gameplay Time"
]

class TypogaDraw:

    title = "Typoga Scores"
    randFilePath = "scores/highScore_random.txt"
    leadFilePath = "scores/highScore_phrases.txt"
    progFilePath = "scores/highScore_programming.txt"

    def __init__(self):
        # Set Window Title and Size
        plt.figure(num=self.title, figsize=(3,6))

    def checkForScoreFiles(self):
        """
        Check if any highscore files exist.
        """
        if not os.path.exists(self.randFilePath) and \
           not os.path.exists(self.leadFilePath) and \
           not os.path.exists(self.progFilePath):
            print("You should first play the game.\n Run ./typoga.sh")
            exit(0)

        self.checkButGO = None
        self.checkButGO = None

        self.pos = 1

    def checkBoxesInit(self):
        """
        Initialize check boxes and click events.
        """
        # Check which score files exist.
        self.checkForScoreFiles()

        # Initialize CheckBox Menu for Game Options
        raxGO = plt.axes([0.02, 0.5, 1, 0.5], frameon = False)
        self.checkButGO = CheckButtons(raxGO, GameOptions, (False, False, False))
        # Set CheckBox handler for game Options
        self.checkButGO.on_clicked(self.handleUserSelection)

        # Initialize CheckBox Menu for Score Options
        raxSO = plt.axes([0.02, 0.05, 1, 0.5], frameon = False)
        self.checkButSO = CheckButtons(raxSO, SocreOptions,
                    (False, False, False, False, False, False, False, False))
        # Set CheckBox handler for game Options
        self.checkButSO.on_clicked(self.handleUserSelection)

    def handleUserSelection(self, label):
        """
        This method is called every time a check box gets pressed. 
        """
        # Draw Random data in its figure
        fig = plt.figure(num=GameOptions[0], figsize=(6,8))
        if self.checkButGO.get_status()[0] == True :
            fig.clear()
            self.parseFile(self.randFilePath)
            fig.show()
        else:
            plt.close()

        # Draw Leaders data in its figure
        fig = plt.figure(num=GameOptions[1], figsize=(6,8))
        if self.checkButGO.get_status()[1] == True :
            fig.clear()
            self.parseFile(self.leadFilePath)
            fig.show()
        else:
            plt.close()

        # Draw Programming data in its figure
        fig = plt.figure(num=GameOptions[2], figsize=(6,8))
        if self.checkButGO.get_status()[2] == True :
            fig.clear()
            self.parseFile(self.progFilePath)
            fig.show()
        else:
            plt.close()

    def parseFile(self, pfile):
        """
        Method used to parse pfile and plot graphics
        """
        # Check if file exists
        if not os.path.exists(pfile):
            print("File %s does not exist" % pfile)
            return
        else:
            hsf = open(pfile,"r")

            lines = hsf.readlines()
            lines = lines[3:] # skip header

            # Reset plot Position
            self.pos = 1
            for i in range(len(self.checkButSO.get_status())):
                scores = [] # Clear previous scores
                if self.checkButSO.get_status()[i] == True:
                    # Parse each score line
                    for scoreLine in lines:
                        scoreLine = scoreLine.strip() # remove \n
                        scoreLine = scoreLine.split(":")

                        scores.append(float(scoreLine[i+1])) # store data
                    # plot scores data in 
                    self.plotData(scores, i)

    def plotData(self, scores, index):
        """
        Plot score data
        """
        if len(scores) == 0:
            scores.append(0)

        # Calculate mean value before appending 0 value at the end
        mean = np.mean(scores)
        # Append zero to get space to print mean value
        scores.append(0)

        x = np.arange(1, len(scores)+1, 1)

        # Divide plot based on user selection
        rows = self.checkButSO.get_status().count(True)
        plt.subplot(rows, 1, self.pos)
        self.pos += 1

        plt.ylabel(SocreOptions[index])
        plt.xticks(x)

        # Draw bar plot
        plt.bar(x, scores)
        # Add text legends to each bar
        for i in range(len(scores)-1): # -1 because we appended zero at the end
            plt.text(i+0.8, scores[i]/2, ("%.02f" % scores[i]), fontsize=8, color='black')

        # Draw orange bar for the highest value
        max_val = np.argmax(scores)
        plt.bar(max_val+1, scores[max_val], color='orange')
        # TODO remove this line:
        # plt.text(max_val+1, scores[max_val], ("%.02f" % scores[max_val]), fontsize=10, color='black')

        # Draw mean line
        plt.plot([0, len(scores)], [mean, mean], 'black')
        plt.text(len(scores), mean, ("%.02f" % mean), fontsize=10, color='black')


    def run(self):
        self.checkBoxesInit()
        #show all
        plt.show()

if __name__ == '__main__':
    """
    """
    td = TypogaDraw()
    td.run()
