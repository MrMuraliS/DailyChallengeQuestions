#!/bin/bash -x

PS4="+ ${BASH_SOURCE} : ${LINENO} : "
black . --exclude hackerrank.sh
git add .
TODAY=$(date +%Y-%m-%d-%H:%M:%S)
git commit -m "Committing changes on $TODAY"
wait
git push
