Typoga
======

Typoga is a different touch typing game.

#### Description

Hey! Try out Typoga! Typoga is touch typing game where you need
to type words as fast as you can. The more accurate and
fast you are, the higher your score. All your scores are saved so
that you can track your progress.

#### Instructions

Run:

\$ ./typoga.sh

Type "?" anytime to exit!
![gameplay](https://github.com/pelco/typoga/blob/master/lib/img/gameplay.gif)

#### Track you progress:

\$ ./stats.py 1
![gameplay](https://github.com/pelco/typoga/blob/master/lib/img/scores.png)

\$ ./stats.py 2
![gameplay](https://github.com/pelco/typoga/blob/master/lib/img/accuracy.png)

Releases:
---------

**v2018.3:**

-   Added option to select game type.

-   Misses are also saved into file in **score/misses_{gametype}.txt**.

-   Score are saved in **score/highScore_{gametype}.txt.**.

-   Score penalization if phrase/words are not typed until the end.

-   Automatically create score files.

-   Added categories based on wpm speed.

-   Words are not counted for wpm if wrongly typed.

-   Created score and lib folder to store the files.

**v2018.2:**

-   Score calculation improvement. Added minimum hit chars to get score,
    calculation of chars per minute.

-   Score is now read/saved to file named **highScore.txt.**.

-   Fixed typos, and minor bugs.

-   Created folder to store the files phrases/words.

-   Reduced some of the phrases in phrases.txt.

**v2018.1:**

-   Initial release.

-   Game implements basic functionality.

-   Based in the script: https://github.com/Orbmancer/bash-typing-game
