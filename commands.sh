#!/bin/bash -xe
PS4="+ ${BASH_SOURCE} : ${LINENO} : "

function CodePush() {
    black . --exclude commands.sh
    git add .
    local TODAY=$(date +%Y-%m-%d-%H:%M:%S)
    git commit -m "Commiting changes on ${TODAY}"
    wait
    git push
}

CodePush
