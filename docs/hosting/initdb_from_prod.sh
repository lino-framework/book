#!/bin/bash
# Copyright 2016-2018 Rumma & Ko Ltd
# initialize this project latest production snapshot

set -e

LOGFILE=/var/log/lino/upgrades.log
OLD=/usr/local/django/ann
NEW=/usr/local/django/bert

echo initdb_from_prod.sh was started `date` >> $LOGFILE

echo PART1 : MIRROR MEDIA FILES
OPTS="-a --verbose --delete --delete-excluded --delete-during --times --log-file $LOGFILE"

function doit {
    nice rsync $OPTS $OLD/$1 $NEW/$1
}

doit media
#doit beid_collect


echo PART2 : DUMP A SNAPSHOT OF $OLD
cd $OLD
. env/bin/activate
python manage.py dump2py -o snapshot2testing


echo PART3 : RESTORE SNAPSHOT TO $NEW
cd $NEW
. env/bin/activate
python manage.py run $OLD/snapshot2testing/restore2testing.py --noinput

echo initdb_from_prod.sh finished `date` >> $LOGFILE
