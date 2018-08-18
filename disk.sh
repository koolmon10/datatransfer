#!/bin/bash

#checks for root privilege (required to read all files in the directory)
if [[ $EUID -ne 0 ]]; then
    echo "Error: Must be root"
    exit 1
fi

arg=""
#functions
getsize() #gets the size of the user directory
    {
    #echo "Getting size"
    size=$( du -sch "$dirname" | awk '{print $1}' )
    echo "$size"
    }
copydata() #copies the data to temp directory
    {
    echo "Copying data"
    }

#parses the arguments
while [ "$1" != "" ]; do
    case $1 in
        --get-size )    
#            echo "--get-size command accepted"
            if [ "$arg" = "" ]; then
                arg="getsize"
            else
                echo "Error: too many arguments"
                exit 1
            fi
            shift
            ;;
        --copy-data )
#            echo "--copy-data command accepted"
            if [ "$arg" = "" ]; then
                arg="copydata"
            else
                echo "Error: too many arguments"
                exit 1
            fi
            shift
            ;;
        * )
            dirname=$1
            shift
#            echo "saving $dirname as \$dirname"
    esac
done

if [ "$arg" != "" ]; then
    $arg
else
    echo "Error: No arguments specified"
    exit 1
fi
exit 0
