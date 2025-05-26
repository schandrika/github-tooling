#!/bin/bash

MY_PATH="$(dirname -- "${BASH_SOURCE[0]}")"
MY_PATH="$(cd -- "$MY_PATH" && pwd)"
PARENT_PATH="$(dirname -- "${MY_PATH}")"

## Absolut path to the file that should replace the one in the repo
REPLACE_FILE=$PARENT_PATH/actions-all-repositories/*

## Relative from any repos root
FILE=.github/workflows

cp $REPLACE_FILE $FILE
