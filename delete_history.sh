#!/bin/sh

# confirm
echo "Are you sure to delete all history? [y/n]"
read -r confirm
if [ "$confirm" != "y" ]; then
    echo "Abort."
    exit 0
fi

# delete
echo "Deleting checkpoint"
rm -rf ./checkpoint/sam/2023*
echo "Deleting logs"
rm -rf ./logs/*
echo "Deleting runs"
rm -rf ./runs/*
echo "Done."