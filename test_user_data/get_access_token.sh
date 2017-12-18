data=$(ssh -i ~/team-playbook/ssh/id_rsa ansible@back-jla.tcs-citadeldev.cloud-omc.org "docker exec -t bdd-container psql synapse --command \"SELECT token FROM access_tokens WHERE user_id='$1';\"")

if [ $data = null ]; then
	echo "NOK"
>> /dev/null
else
	echo $data
fi