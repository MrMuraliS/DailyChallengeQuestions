#!/bin/bash -x

PS4='EXECUTING: '
black . --exclude hackerrank.sh &&
git add . &&
TODAY=$(date +%Y-%m-%d-%H:%M:%S) &&
git commit -m "Committing changes on $TODAY"
wait
git push
