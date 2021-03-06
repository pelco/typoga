#!/bin/bash

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

# The values reflect km/h
declare -A category
for i in {0..4}; do category[$i]="a Snail"; done
for i in {5..9}; do category[$i]="a Walking person"; done
for i in {10..14}; do category[$i]="a Jogger"; done
for i in {15..19}; do category[$i]="a Bicycle"; done
for i in {20..29}; do category[$i]="a Dog"; done
for i in {30..44}; do category[$i]="Usain Bolt"; done
for i in {45..49}; do category[$i]="a Fox"; done
for i in {50..64}; do category[$i]="a Tiger"; done
for i in {65..69}; do category[$i]="a Gazelle"; done
for i in {70..79}; do category[$i]="a Horse"; done
for i in {80..120}; do category[$i]="a Cheath"; done
function getCategory {
    echo "${green}${category[$1]}${reset} ($1)"
}
