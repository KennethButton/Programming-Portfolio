#!/bin/bash

###########################################################
# 1_getJournal.sh
#-----------------------------
# Returns the journal for sshd as long back as possible and
# overwrites the previous journal snapshot for space.
#
# Not yet implemented:
# 	-b	compress previous snapshot to /bkup/ folder
# Implemented:
#
###########################################################

echo SecScan-1 i: Reminder: All SecScan scripts require sudo or root.
echo SecScan-1 i: ----------------------------------------------------
echo SecScan-1 i: Now grabbing all entries within journalctl that
echo SecScan-1 i: relate to sshd that have an IP address within them.

journalctl | grep sshd | grep -E --regexp="([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)" > results/journalScan

echo SecScan-1 i: Journal Scan Completed.
