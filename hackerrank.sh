PS4='EXECUTING: '
set -x
black . --exclude hackerrank.sh &&
git add . &&
TODAY=$(date +%Y-%m-%d-%H-%M-%S) &&
git commit -m "Committing changes on $TODAY" &&
git push
