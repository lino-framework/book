=====================
Backup and monitoring
=====================

How to configure a backup and monitoring service that will monitor and backup
the production sites of your customers.

In the following examples we  assume that the service is running on your server
`example.com`.

On the backup server, we create a user named "mirror" and a ssh key pair::

    $ sudo useradd -d /mnt/disk/snapshots_collection/ mirror
    $ mkdir /mnt/disk/snapshots_collection/.ssh
    $ ssh-keygen -t rsa -b 4096 -C "mirror@example.com"

When the prompt ask for where to store the key, we need to choose the home
directory of the mirror user::

    $ Enter file in which to save the key (/home/hamza/.ssh/id_rsa): /mnt/disk/snapshots_collection/.ssh/id_rsa

And for the target user we need to create the same user "mirror" which should
have the read permission to the snapshots::

    $ sudo useradd -m -d /home/mirror -s /bin/bash mirror
    $ sudo mkdir /home/mirror/.ssh/

Add the ssh key pair of mirror from example.com to the authorized_keys of the target server::

    $ cat ~/.ssh/id_rsa.pub | ssh username@myawesomelinosite.com 'cat >> ~/.ssh/authorized_keys'

We need also to fix permission issues::

    $ sudo chown -R mirror:mirror /home/mirror/.ssh

By default, this will generate the ssh key file in /home/you/.ssh/id_rsa. Then,
we need to add this to the authorized_keys of the lino host server::

    $ cat ~/.ssh/id_rsa.pub | ssh username@myawesomelinosite.com 'cat >> ~/.ssh/authorized_keys'

If we are using monit , we can add a check about old snapshots (more than one
day)::

    $ #/bin/bash
    $ # designed to run as cron job
    $ set -e
    $ TARGET=/mnt/disk/snapshots_collection
    $ if [[ $(find $TARGET -mtime +1 -print) ]]; then
    $   echo "File $filename exists and is older than one day"
    $ fi
