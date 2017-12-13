#!/usr/bin/env bash

test_run=""
verbose=0
all=0

if [ $# = 0 ];
then
	echo "Écrivez le nom de votre infra : "
	read infra

else
	for arg in $@;
	do
		if "$arg" = *"-"* ;
		then
			
			if "$arg" = "-v" ;
			then
				verbose=1
			fi

			if  "$arg" = "-a" ;
			then
				all=1
			fi

		else
			test_run=$arg
		fi
	done
fi

echo $verbose
echo $all
echo $test_run