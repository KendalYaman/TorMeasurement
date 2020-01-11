#!/bin/sh
if [ "$#" -ne 2 ]; then
  echo "not correct argument number" 
  exit 1
fi

exec zcash-cli sendmany "" "{\"$2\":$1}"