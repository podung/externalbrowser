#!/usr/bin/env bash

echo "*******************"
echo "env vars outside of poetry/python just in bash....."
printenv
echo "*******************"
poetry run python externalbrowser/main.py

while true
do
  echo "wait"
  sleep 1
done
