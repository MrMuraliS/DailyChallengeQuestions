PS4='Executing: '
#set -x
black . --exclude hackerrank.sh &&
git add . &&
TODAY=$(date +%Y-%m-%d-%H-%M-%S) &&
git commit -m "Hacker Rank Questions on $TODAY" &&
git push
