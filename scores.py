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
        plt.figure(num=self.title, figsize=(16,8))

    def checkForScoreFiles(self):
        """
        Check if any highscore files exist.
        """
        if not os.path.exists(self.randFilePath) and \
           not os.path.exists(self.leadFilePath) and \
           not os.path.exists(self.progFilePath):
            print("You should first play the game.\n Run ./typoga.sh")
            exit(0)

    def checkBoxesInit(self):
        """
        """
        # Check which score files exist.
        self.checkForScoreFiles()

        # Initialize CheckBox Menu for Game Options
        raxGO = plt.axes([0.01, 0.8, 0.1, 0.15], frameon = False, title = WINDOW_TITLE)
        self.checkButGO = CheckButtons(raxGO, gameOptions, (False, False, False))
        # Set CheckBox handler for game Options
        self.checkButGO.on_clicked(self.handleUserSelection)

        # Initialize CheckBox Menu for Score Options
        raxSO = plt.axes([0.01, 0.6, 0.1, 0.2], frameon = False)
        self.checkButSO = CheckButtons(raxSO, socreOptions,
                    (False, False, False, False, False, False, False, False))
        # Set CheckBox handler for game Options
        self.checkButSO.on_clicked(self.handleUserSelection)

    def handleUserSelection(self, label):
        """
        """
        print(self.checkButGO.get_status())
        print(self.checkButSO.get_status())
        #fig = plt.figure(num=WINDOW_TITLE)
        #fig.clear()
        print(self.checkButSO.get_status().count(True))

        # Divide plot based on user selection
        cols = self.checkButGO.get_status().count(True) 
        rows = self.checkButSO.get_status().count(True)

        # Draw Random selected data
        if self.checkButGO.get_status()[0] == True :
            self.parse_file(self.randFilePath, cols, rows)

        # Draw Leaders selected data
        if self.checkButGO.get_status()[1] == True :
            self.parse_file(self.leadFilePath, cols, rows)

        # Draw Programming selected data
        if self.checkButGO.get_status()[2] == True :
            self.parse_file(self.progFilePath, cols, rows)

        plt.draw()

    #def parse_file(self, pfile, pos, index, title):
    def parse_file(self, pfile, cols, rows):
        """
        Method used to parse pfile and draw grafics
        """
        scores=[]
         # Check if file exists
        if not os.path.exists(pfile):
            print("File %s does not exist" % pfile)
            return
        else:
            hsf = open(pfile,"r")

            lines = hsf.readlines()
            lines = lines[3:] # skip header

            scores=[]
            # Read every line
            for line in lines:
                #print line
                line = line.strip() # remove \n
                line = line.split(":")

                scores.append(float(line[index])) # store data

        if len(scores) == 0:
            scores.append(0)

        # Calculate mean value before appending 0 value at the end
        mean = np.mean(scores)
        # Append zero to get space to print mean value
        scores.append(0)

        x = np.arange(1,len(scores)+1)

        plt.subplot(3, 1, pos)
        plt.ylabel(title)
        # Set sitle
        plt.title(pfile.split('_')[1].split('.')[0])

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