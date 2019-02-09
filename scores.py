#!/usr/bin/env python3
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

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
PH_LEADERS = "Ph Leaders"
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
        Check if highscore files exist. If not remove it form selection.
        """
        if not os.path.exists(self.randFilePath):
            gameOptions.remove(RANDOM)

        if not os.path.exists(self.leadFilePath):
            gameOptions.remove(PH_LEADERS)

        if not os.path.exists(self.progFilePath):
            gameOptions.remove(PROGRAMMING)
        
        # If no options are available tell user to the play game.
        if len(gameOptions) == 0:
            print("You should first play the game.\n Run ./typoga.sh")
            exit(0)

    def checkBoxesInit(self):
        """
        """
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
        print(label)
        if label == RANDOM:
            print("Rand")
        elif label == PH_LEADERS:
            print("Lead")
        elif label == PROGRAMMING:
            print("Prog")
        plt.draw()

    def run(self):
        self.checkBoxesInit()
        #show all
        plt.show() 

if __name__ == '__main__':
    """
    """
    td = TypogaDraw()
    td.run()