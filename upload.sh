#!/bin/bash

gitoken=$(~/token1)

git add .
git commit -m "answer"

echo $token
git push

read -p "done"
