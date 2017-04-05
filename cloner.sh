#!/bin/bash
# run pull.py first then run this script

while read p; do
    a=`echo "$p"| tr '/' '\n' | tail -n2`
    echo $a
    git clone $p ~/Projects/$a
    done <git_repo.txt
