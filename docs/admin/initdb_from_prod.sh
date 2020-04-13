#!/bin/bash
# Copyright 2016-2020 Rumma & Ko Ltd
# initialize this project latest production snapshot

set -e

LOGFILE=/var/log/lino/upgrades.log
OLD=/usr/local/django/ann
NEW=/usr/local/django/bert

echo initdb_from_prod.sh was started `date` >> $LOGFILE

echo PART1 : MAKE A SNAPSHOT OF $OLD
cd $OLD
. env/bin/activate
python manage.py dump2py -o snapshot2preview

echo PART2 : MIRROR MEDIA FILES AND SNAPSHOT
OPTS="-a --verbose --delete --delete-excluded --delete-during --times --omit-dir-times --log-file $LOGFILE"

function doit {
    nice rsync $OPTS $OLD/$1 $NEW/
}

doit media
doit snapshot2preview


echo PART3 : RESTORE SNAPSHOT TO $NEW
cd $NEW
. env/bin/activate
python manage.py run snapshot2preview/restore2preview.py --noinput
python manage.py collectstatic --noinput

echo initdb_from_prod.sh finished `date` >> $LOGFILE
