#!/bin/bash

gitoken=$(cat ~/token1)

git add .
git commit -m "answer"

echo $gittoken
#git push

read -p "done"
