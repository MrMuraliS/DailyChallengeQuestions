black . --exclude hackerrank.sh &&
git add . &&
TODAY=$(date +%Y-%m-%d-%H-%M-%S) &&
echo "This is sample Test $TODAY"
git commit -m "Hacker Rank Questions on $TODAY" &&
git push
