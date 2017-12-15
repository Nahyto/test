#!/bin/bash


data=$(curl 'https://ptl-test.citadel.team/api/get_domain.php?email='$1)
if [ $data = null ]; then
	echo "NOK"
>> /dev/null
else
	domain=$(echo $data | cut -d'"' -f4)
	echo $domain
fi
