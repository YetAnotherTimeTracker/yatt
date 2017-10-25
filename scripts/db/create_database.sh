#!/bin/bash

db_user=yatt_user
db_password=root
db_name=yatt_db
db_host="localhost"
db_port=5432


psql -c "DROP DATABASE IF EXISTS $db_name"
psql -c "DROP OWNED BY $db_user"
psql -c "DROP USER IF EXISTS $db_user"


echo "Creating user"

psql -c "CREATE ROLE $db_user WITH LOGIN PASSWORD '$db_password'"
psql -c "ALTER ROLE $db_user CREATEDB"


echo "Creating db"

psql -c "CREATE DATABASE $db_name"
psql -c "GRANT ALL PRIVILEGES ON DATABASE $db_name TO $db_user"


echo "All done"
