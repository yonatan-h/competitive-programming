#!/bin/bash

GIT_TOKEN=$(cat ~/token1)

git add .
git commit -m "answer"

echo "---"
echo $GIT_TOKEN
echo "---"
git push

read -p "done"
