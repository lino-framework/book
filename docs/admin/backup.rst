=====================
Backup and monitoring
=====================

How to configure a backup and monitoring service that will monitor and backup
the production sites of your customers.

Each customer who wants to use our service must create a user "mirror" on their
server that we will use to connect to their server::

    $ sudo adduser mirror
    $ sudo adduser mirror www-data
    $ sudo -u mirror mkdir /home/mirror/.ssh/

The customer must also have a daily snapshot cron job (:doc:`snapshot`) and
communicate us the full path of the snapshot file(s) they want us to backup.

Setting up the backup server
============================

In the following examples we assume that the service is to be running on your
server `example.com`.

On the backup server, we create a user named "mirror" and a ssh key pair::

    $ sudo adduser -d /mnt/disk/mirror/ mirror
    $ mkdir /mnt/disk/mirror/.ssh
    $ ssh-keygen -t rsa -b 4096 -C "mirror@example.com"

By default, this will generate the ssh key file in /home/you/.ssh/id_rsa. When
the prompt ask for where to store the key, we need to choose the home directory
of the mirror user::

    $ Enter file in which to save the key (/home/hamza/.ssh/id_rsa): /mnt/disk/mirror/.ssh/id_rsa

Create an executable file :file:`collect_snapshots.sh` with this content::

  #/bin/bash
  # designed to run as cron job
  set -e
  TARGET=/mnt/disk/mirror/snapshots

  # one rsync for each customer:
  echo customer1
  rsync --times --progress mirror@customer1:/customer1/path/to/snapshot.zip $TARGET/snapshots/customer1/
  echo customer2
  rsync --times --progress mirror@customer2:/customer2/path/to/snapshot.zip $TARGET/snapshots/customer2/

Add the ssh key pair of mirror@example.com to the authorized_keys of each
customer server::

    $ cat ~/.ssh/id_rsa.pub | ssh username@customersite.com 'cat >> ~/.ssh/authorized_keys'

Add a daily cron job in /etc/cron.daily::

  #!/bin/sh
  sudo -u mirror /mnt/disk/mirror/collect_snapshots.sh > /dev/null

If we are using `monit`, we can add a check about old snapshots (more than one
day)::

    #/bin/bash
    # designed to run as cron job
    set -e
    TARGET=/mnt/disk/mirror/snapshots
    if [[ $(find $TARGET -mtime +1 -print) ]]; then
      echo "File $filename exists and is older than one day"
    fi
