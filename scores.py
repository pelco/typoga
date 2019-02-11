#!/usr/bin/env python3
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
############################################################
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(6*np.pi*t)

fig, ax = plt.subplots()
l0, = ax.plot(t, s0, visible=False, lw=2)
l1, = ax.plot(t, s1, lw=2)
l2, = ax.plot(t, s2, lw=2)
plt.subplots_adjust(left=0.2)

rax = plt.axes([0.05, 0.4, 0.1, 0.15])
check = CheckButtons(rax, ('2 Hz', '4 Hz', '6 Hz'), (False, True, True))


def func(label):
    if label == '2 Hz':
        l0.set_visible(not l0.get_visible())
    elif label == '4 Hz':
        l1.set_visible(not l1.get_visible())
    elif label == '6 Hz':
        l2.set_visible(not l2.get_visible())
    plt.draw()
check.on_clicked(func)

# plt.show()
plt.close()
###########################################################

WINDOW_TITLE = "Game Options"

# Game Options
RANDOM = "Random"
PH_LEADERS = "Leaders"
PROGRAMMING = "Programming"

gameOptions = [
    RANDOM,
    PH_LEADERS,
    PROGRAMMING ]

socreOptions = [
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
        """
        # Check which score files exist.
        self.checkForScoreFiles()

        # Initialize CheckBox Menu for Game Options
        raxGO = plt.axes([0.02, 0.5, 1, 0.5], frameon = False)
        self.checkButGO = CheckButtons(raxGO, gameOptions, (False, False, False))
        # Set CheckBox handler for game Options
        self.checkButGO.on_clicked(self.handleUserSelection)

        # Initialize CheckBox Menu for Score Options
        raxSO = plt.axes([0.02, 0.05, 1, 0.5], frameon = False)
        self.checkButSO = CheckButtons(raxSO, socreOptions,
                    (False, False, False, False, False, False, False, False))
        # Set CheckBox handler for game Options
        self.checkButSO.on_clicked(self.handleUserSelection)

    def handleUserSelection(self, label):
        """
        """    

        # Divide plot based on user selection
        rows = self.checkButSO.get_status().count(True)
  
        # Draw Random selected data
        fig = plt.figure(num=gameOptions[0])
        if self.checkButGO.get_status()[0] == True :
            self.pos = 1
            fig.clear()
            self.parseFile(self.randFilePath, rows)
            fig.show()
        else:
            plt.close()

        # Draw Leaders selected data
        fig = plt.figure(num=gameOptions[1])
        if self.checkButGO.get_status()[1] == True :
            self.pos = 1
            fig.clear()
            self.parseFile(self.leadFilePath, rows)
            fig.show()
        else:
            plt.close()

        # Draw Programming selected data
        fig = plt.figure(num=gameOptions[2])
        if self.checkButGO.get_status()[2] == True :
            self.pos = 1
            fig.clear()
            self.parseFile(self.progFilePath, rows)
            fig.show()
        else:
            plt.close()

        plt.draw()
        

    #def parseFile(self, pfile, pos, index, title):
    def parseFile(self, pfile, rows):
        """
        Method used to parse pfile and draw grafics
        """
        # Check if file exists
        if not os.path.exists(pfile):
            print("File %s does not exist" % pfile)
            return
        else:
            hsf = open(pfile,"r")

            lines = hsf.readlines()
            lines = lines[3:] # skip header

            #scores = []
            # Read every line
            # for scoreLine in lines:
            #     scoreLine = scoreLine.strip() # remove \n
            #     scoreLine = scoreLine.split(":")
            #     print(scoreLine)
            #     for i in range(len(self.checkButSO.get_status())):
            #         # Parse all selected Score options
            #         if self.checkButSO.get_status()[i] == True:
            #             scores.append(float(scoreLine[i+1])) # store data

            for i in range(len(self.checkButSO.get_status())):
                scores = []
                if self.checkButSO.get_status()[i] == True:
                    for scoreLine in lines:
                        scoreLine = scoreLine.strip() # remove \n
                        scoreLine = scoreLine.split(":")

                        scores.append(float(scoreLine[i+1])) # store data

                    self.plotData(scores, rows, i)
    
    def plotData(self, scores, rows, index):
        """
        """
        if len(scores) == 0:
            scores.append(0)

        # Calculate mean value before appending 0 value at the end
        mean = np.mean(scores)
        # Append zero to get space to print mean value
        scores.append(0)

        x = np.arange(1, len(scores)+1)
        
        plt.subplot(rows, 1, self.pos)
        self.pos += 1

        plt.ylabel(socreOptions[index])
        plt.xlabel('n Games played')
        # Draw bar plot
        plt.bar(x, scores)
        # Draw orange bar for the highest value
        max_val = np.argmax(scores)
        plt.bar(max_val+1, scores[max_val], color='orange')
        plt.text(max_val+1, scores[max_val], ("%.02f" % scores[max_val]), fontsize=10, color='black')

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