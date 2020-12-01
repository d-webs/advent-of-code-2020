#!/usr/bin/env sh

DAY=$(date +%d | sed 's/^0*//')
BASE_URL="https://adventofcode.com/2020/day/${DAY}/input"

curl --create-dirs -o lib/day$DAY/input.txt $BASE_URL
