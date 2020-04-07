#!/bin/bash

# ensure db is up-to-date and running
while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Upgrade command failed, retrying in 5 secs...
    sleep 5
done

# run gunicorn web server
exec gunicorn -b 5001:5001 wsgi:app