# Function that initializes misFile at the beginning of each phrase
function init_miss_f {
    echo "" >> $misFile
    echo -n "$startTime,$rNum:" >> $misFile
}
# Function that writes missed chars to misse file
function write_miss {
    # writr characterIndex, charToHit, charTyped
    echo -n "[$i:$wordChar:$char]," >> $misFile
}
# Update word count to calculate wpm
function upWordCount {
    if [ $wrongWord -eq 0 ]; then
        ((wordCount++))
    fi
    wrongWord=0
}
# Check if files to store highscores and misses exist
function checkScoresFile {
    # File to read/write highScores.
    hsFile="scores/highScore_$(echo $1 | awk -F'/' '{ print $2 }')"
    # File to store misses
    misFile="scores/misses_$(echo $1 | awk -F'/' '{ print $2 }')"
    # If file does not exist create from base files
    if [ ! -f $hsFile ]; then
        cp -f scores/highScore.txt $hsFile
    fi
    if [ ! -f $misFile ]; then
        cp -f scores/misses.txt $misFile
    fi
}
