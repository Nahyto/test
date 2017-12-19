USERID=$1
INFRA=$2
ACCESS_TOKEN=$(ssh -o "StrictHostKeyChecking=no" -i ~/team-playbook/ssh/id_rsa ansible@back-$INFRA.tcs-citadeldev.cloud-omc.org 'bash -s' < get_access_token.sh $USERID)
echo $ACCESS_TOKEN
