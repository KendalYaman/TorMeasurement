#!/bin/sh
if [ "$#" -ne 1 ]; then
  echo "not correct argument number" 
  exit 1
fi

exec zcash-cli z_getbalance "$1"