#!/bin/sh
if [ "$#" -ne 3 ]; then
  echo "not correct argument number" 
  exit 1
fi

exec zcash-cli z_sendmany "$2" "[{\"amount\": $1 , \"address\": \"$3\"}]"