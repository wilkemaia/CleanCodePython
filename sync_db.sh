#!/bin/bash
SRC=~/CleanCodePython/schema.db
DEST="/mnt/c/Users/Wilke/Documents/sqlite_sync/schema.db"

cp $SRC $DEST
echo "Banco sincronizado em $DEST"
