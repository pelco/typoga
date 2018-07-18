#!/bin/bash

IFS=$'\n'

red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
reset=`tput sgr0`

MinChar2Score=80 # Minimum number of chars to hit

# Every time user reaches multiple of MinChar2Score 
# the Score is increased +1%:  1 -> 1%, 2 -> 2%
scFactor=0

hitChar=0 # Saves the total of hit characters
wordCount=-1 # Number of correct words completed
wrongWord=0 # Indicates if word was wrongly typed
missedChar=0 # Number of times you miss the character

# Indicates if phrase was typed until the end. Penalize score 10% if not.
incompletePhrase=0

# Load functions
source lib/functions.sh

clear
echo ""
printf "Welcome to Typoga. Type as fast as you can.\n\n"

# Get list of Phrases/Words
options=("Random" "Phrases for Leaders" "Programming Keywords" "Exit")
select opt in "${options[@]}"
do
    case $opt in
        "Random")
            fileW='words_phrases/random.txt'
            break
            ;;
        "Phrases for Leaders")
            fileW='words_phrases/phrases.txt'
            break
            ;;
        "Programming Keywords")
            fileW='words_phrases/programming.txt'
            break
            ;;
        "Exit")
            exit 0
            ;;
        *)
            echo "Invalid Option"
            ;;
  esac
done
echo ""

# Read the file
words=(`cat $fileW`)
# Get total cdnumber of lines
NUMBER_OF_LINES=$(wc -l $fileW | cut -f1 -d' ')

# Check if we have a place to store/read scores
checkScoresFile $fileW

# Read Highest score
hscore=$(head -n 2 $hsFile | sed -n -e 2p | awk -F ':' '{print $2}')

echo "Score to Beat: ${green}$hscore${reset}"
echo "Press '?' any time to finish game."
read -n 1 -s -p "Press any key to start "
echo ""

################__GAME__################

startTime=`date +%s`
while true;do

    # Get random word every time
    rNum=$(( $RANDOM % $NUMBER_OF_LINES ))
    word=${words[rNum]}

    # Initialize miss file
    init_miss_f

    # Check if last word correctly typed and update word count
    upWordCount
    echo ": ${word}"
    echo -n ": "
    incompletePhrase=0 # Here we are at beginning of a phrase
    for i in `seq 0 $(( ${#word} -1 ))`; do
        read -n 1 -s char

        # Check if user wants to end game.
        if [ "$char" == "?" ]; then
            break
        fi
        incompletePhrase=1 # User started typing phrase, mark as incomplete
        wordChar="${word:$i:1}"

        # Increase score by +10%
        if [ $(($hitChar%$MinChar2Score)) -eq 0 ] && [ ! $hitChar -eq 0 ]; then
            ((scFactor++))
        fi

        if [ "$char" == "$wordChar" ]; then
            printf "${green}${wordChar}${reset}"
            ((hitChar++))
            # Count words when dealing with phrases
            if [ "$wordChar" == " " ]; then
                # Check if last word correctly typed and update word count
                upWordCount
            fi
        else
            # Print "_" when missing a space
            if [ "$wordChar" == " " ]; then
                printf "${red}_${reset}"
                wrongWord=0
            else
                # Print the missed character in yellow if capitalization is wrong
                if [ "${char^^}" == "$wordChar" ] || [ "${char,,}" == "$wordChar" ]; then
                    printf "${yellow}${wordChar}${reset}"
                else
                    printf "${red}${wordChar}${reset}"
                fi
                wrongWord=1 # Signalize wrong word typed
            fi
            # Count number of times missed
            ((missedChar++))
            # Store miss to file
            write_miss
        fi
    done

    if [ "$char" == "?" ]; then
        printf "\n\n"
        break
    fi
    echo ""
done
endTime=`date +%s`
runtimeSec=$((endTime-startTime))
totalChar=$((hitChar+missedChar))

#################__SCORE__################
# Only show score wit we reach at least once MinChar2Score and started playing it
if [ $scFactor -gt 0 ] && [ $hitChar -gt 0 ]; then
    # Calculate Accuracy
    acc=$(echo "scale=2; acc = (${hitChar}*100)/${totalChar}; acc" | bc)
    echo "Accuracy: (${hitChar}/${totalChar}) = $acc %"

    # Calculate Words/Characters Per Minute
    wpm=$(echo "scale=2; spe = (${wordCount}*60)/${runtimeSec}; spe" | bc)
    cpm=$(echo "scale=2; spe = (${hitChar}*60)/${runtimeSec}; spe" | bc)
    echo "Speed: $wpm wpm, $cpm cpm"

    # Calculate Score
    sc=$(echo "scale=2; acc = (${hitChar}*100)/${totalChar};
    spe = (${hitChar}*60)/${runtimeSec};
    scf = ${scFactor}/100 + 1 - ${incompletePhrase}/10;
    var3 = acc*spe*scf;
    var3" | bc)

    # Store results into the file
    # epochTime:score:acc:wpm:cpm:n_Words:n_hitChars:n_missedChars:runTime
    result="$startTime:$sc:$acc:$wpm:$cpm:$wordCount:$hitChar:$missedChar:$runtimeSec"
    echo $result >> $hsFile
    # Replace high score)
    if [ "$(echo "$sc>$hscore" | bc -l)" -eq 1 ]; then
        echo "Score: $sc ${green}New High Score!${reset}"
        sed -i "2s/.*/$result/" $hsFile
    else
        echo "Score: $sc "
    fi

    echo -n "Your Category: "
    getCategory ${wpm%\.*}
else
    echo "You hit $hitChar characters, you need at least $MinChar2Score to get a score."
fi

exit 0
