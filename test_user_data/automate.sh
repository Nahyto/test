#!/usr/bin/env bash

if [ $# = 0 ]
then
	echo "Hello"
else
	for arg in $@;
	do
		if[ $arg = "-v" ]
then

		fi

		if[ $arg="-a" ]
		then
			for f in *.py; 
			do 
				python "$f"; 
			done
		fi
	done
fi