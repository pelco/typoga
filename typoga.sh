#!/bin/bash

IFS=$'\n'

green=`tput setaf 2`
reset=`tput sgr0`

MinChar2Score=20 # Minimum number of chars to get score

# Every time user reaches multiple of MinChar2Score 
# the Score is increased +10%: 1 -> 10%, 2 -> 20%
scFactor=0

score=0 # Stores the number of times you press the keyboard
maxScore=0 # Stores the total number of characters 
wordCount=-1 # Number of words completed

# File to get list of words or phrases
filew='phrases.txt'
#filew='programing.txt'

# Read the file
words=(`cat $filew`)

NUMBER_OF_LINES=$(wc -l $filew | cut -f1 -d' ')

echo "Press '?' any time to exit."
read -n 1 -s -p "Press any key to continue"
echo ""

startTime=`date +%s`
while true;do

    # Get Random Word every time
    rNum=$(( $RANDOM % $NUMBER_OF_LINES ))
	word=${words[rNum]}
    
    ((wordCount++))
	echo ": ${word}"
    
	for i in `seq 0 $(( ${#word} -1 ))`; do
        
        # Check if user wants to end game.        
        while [ "$char" != "?" ];do
            read -n 1 -s char

            wordChar="${word:$i:1}"
            
            if [ "$char" != "?" ]; then
                ((maxScore++))
            fi
            
            # Increase score by +10%
            if [ $(($maxScore%$MinChar2Score)) -eq 0 ];then
                ((scFactor++))
            fi
            
            if [ "$char" == $wordChar ]; then
                printf "${green}${wordChar}${reset}"
                ((score++))
                # Count words when dealing with phrases
                if [ "$char" == " " ]; then
                    ((wordCount++))
                fi
                break
            else
                #Remove score points for each missed character of the word
                if [ ! "$score" -eq 0 ];then
                     ((score--))
                fi
            fi
        done
	done

    if [ "$char" == "?" ]; then
        printf "\n"
        break
    fi
    echo ""
done

endTime=`date +%s`
runtimeMin=$((endTime-startTime))
#########################################
if [ "$scFactor" -gt 0 ]; then
    # Calculate Accuracy
    echo -n "Accuracy (%): (${score}/${maxScore}) = "
    echo "scale=2; acc = (${score}*100)/${maxScore}; acc" | bc ;

    # Calculate Words Per Minute
    echo -n "Speed (wpm): "
    echo "scale=2; spe = (${wordCount}*60)/${runtimeMin}; spe" | bc

    # Calculate Score
    echo -n "Score: "
    echo "scale=2; acc = (${score}*100)/${maxScore};
    spe = (${wordCount}*60)/${runtimeMin};
    scf = ${scFactor}/10 + 1;
    var3 = acc*spe*scf;
    var3" | bc
else
    echo "You need to reach a lest $MinChar2Score characters to get a score"
fi

