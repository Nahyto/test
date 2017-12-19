USERID=$1
ACCESS_TOKEN=$(ssh -o "StrictHostKeyChecking=no" -i ~/team-playbook/ssh/id_rsa ansible@back-jla.tcs-citadeldev.cloud-omc.org 'bash -s' < get_access_token.sh $USERID)
echo $ACCESS_TOKEN