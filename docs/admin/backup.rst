=====================
Backup and monitoring
=====================

How to configure a backup and monitoring service that will monitor and backup
the production sites of your customers.

In the following examples we  assume that the service is running on your server
`example.com`.

On the backup server, we create a user named "mirror" and a ssh key pair::

    $ sudo useradd -d /mnt/disk/mirror/ mirror
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

  echo customer1
  rsync --times --progress mirror@customer1:/customer1/path/to/snapshot.zip $TARGET/snapshots/customer1.zip
  echo customer2
  rsync --times --progress mirror@customer2:/customer2/path/to/snapshot.zip $TARGET/snapshots/customer2.zip


On each customer server we need to create a user "mirror" which should have the
read permission to the snapshots::

    $ sudo adduser mirror
    $ sudo mkdir /home/mirror/.ssh/

Add on the backup server run the following to add  the ssh key pair of
mirror@example.com to the authorized_keys of the customer server::

    $ cat ~/.ssh/id_rsa.pub | ssh username@customersite.com 'cat >> ~/.ssh/authorized_keys'

We need also to fix permission issues::

    $ sudo chown -R mirror:mirror /home/mirror/.ssh

If we are using `monit`, we can add a check about old snapshots (more than one
day)::

    $ #/bin/bash
    $ # designed to run as cron job
    $ set -e
    $ TARGET=/mnt/disk/mirror/snapshots
    $ if [[ $(find $TARGET -mtime +1 -print) ]]; then
    $   echo "File $filename exists and is older than one day"
    $ fi


Add a daily cron job in /etc/cron.daily::

  #!/bin/sh
  sudo -u mirror /mnt/disk/mirror/collect_snapshots.sh > /dev/null
