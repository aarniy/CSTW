#!/bin/bash

filename="generated_random_bash.txt"
maxsize=$((1024 * 1024))  # 1 MB in bytes
currentsize=0

# Create an empty file
> "$filename"

# Keep appending random numbers until the file size reaches 1 MB
while [ $currentsize -lt $maxsize ]; do
    echo $RANDOM >> "$filename"
    currentsize=$(stat -c%s "$filename")
done

echo "1 MB random file created as $filename"
