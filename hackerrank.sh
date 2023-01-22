black . --exclude hackerrank.sh &&
git add . &&
echo "This is sample Test"
TODAY=$(date +%Y-%m-%d-%H-%M-%S) &&
git commit -m "Hacker Rank Questions on $TODAY" &&
git push
