Typoga
======

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7d837401dd8946a28f55be56836a857e)](https://app.codacy.com/project/pelco/typoga/dashboard)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/pelco/typoga/raw/master/LICENSE)

Typoga is a touch typing game.

# Description

Hey! Typoga is touch typing game where type as fast as you can.
All your scores are saved so that you can track your progress.

# Setup

Install python 3:
```bash
sudo apt-get install python3 python3-pip python3-tk
```

Install packages:
```bash
pip3 install matplotlib numpy
```

# Instructions

Run:

\$ ./typoga.sh

Type "?" anytime to exit!
![gameplay](https://github.com/pelco/typoga/blob/master/lib/img/gameplay.gif)

# Track you progress

\$ ./scores.py

Releases
---------

**v2018.4:**

-   Added new list of RANDOM phrases.

-   Capitalization errors are shown as yellow.

-   Added tool to show statistics/progress information.

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

-   Based in the script: [bash-typing-game](https://github.com/Orbmancer/bash-typing-game)
