#!/bin/bash

# Replace with the IP address of the remote host
REMOTE_HOST="192.168.0.215"

# List of files to copy
FILES=("../../etc/sysctl.conf"\
 "../../var/unbound/etc/unbound.conf"\
 "../../etc/dhcpd.conf"\
 "../../etc/hostname.bse0"\
 "../../etc/hostname.bwfm0"\
 "../../etc/hostname.ure0"\
 "pf.conf"\
 "arp.txt")

# Use SCP to copy files
for file in "${FILES[@]}"; do
  scp $REMOTE_HOST:$file .
done
