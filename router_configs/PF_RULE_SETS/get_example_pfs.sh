#!/bin/bash

# Replace with the IP address of the remote host
REMOTE_HOST="192.168.0.215"

# List of files to copy
FILES=("pf01-simple-set.conf"\
 "pf02-simple-set-with-alias.conf")

# Use SCP to copy files
for file in "${FILES[@]}"; do
  scp $REMOTE_HOST:$file .
done
