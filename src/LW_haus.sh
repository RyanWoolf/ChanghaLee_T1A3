#!/bin/bash
clear
count() {
    local sec=2
    while [ $sec -ge 0 ]; do
        echo -ne " .. $sec\033[0K\r"
        let "sec=sec-1"
        sleep 1
    done
}

echo "

Welcome to LW haus project!

You're about to launch the game.

But before we start, Let's check whether your system is ready

"
sleep 1
echo "Giving permission to execute LW_haus.sh "
chmod +x LW_haus.sh
sleep 1
echo "Permission granted"
sleep 1
echo "Checking Python3 .. Standby "
count
if [[ -x "$(command -v python3 --version)" ]]
then
    echo "Ready to launch"
    FILE="./.venv"
    if [ -d "$FILE" ];then
        echo "Activating venv"
        source .venv/bin/activate
        echo "Initiating the program"
        count
        python3 main.py
    else
        python3 -m venv .venv
        echo "Created virtual evironment"
        count
        echo "Activate venv"
        source .venv/bin/activate
        echo "Install packages .."
        python3 -m pip install art==5.7
        echo "Initiating the program"
        count
        python3 main.py
    fi
else
    echo "

    It requires Python3 to run this game. 

    Please visit "https://www.python.org/downloads/" to download the latest version. 

    Then try again.

    " >&2
fi
