#!/bin/bash
USERID=$1
docker exec -i bdd-container /bin/bash -c 'psql synapse -t -c "select token from access_tokens where user_id = "'"\'$USERID\'"'" order by id desc limit 1;"';