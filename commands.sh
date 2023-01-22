PS4='EXECUTING: '
set -x
black . --exclude hackerrank.sh &&
git add . &&
set +x
TODAY=$(date +%Y-%m-%d, %H:%M:%S) &&
set -x
git commit -m "Committing changes on $TODAY"
wait
git push
