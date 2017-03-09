#!/bin/bash
set -e  # exit on error

if [ "$1" = "-h"  -o "$1" = "--help" ]
then
    cat <<USAGE
Usage:
  $0 [ <envname> ]

When invoked with an envname, then it creates both that virtualenv and
a directory repositories.

Without an envname it assumes that you want to install Lino into the
current environment and that you are in your existing repositories
directory.

USAGE
    exit -1
fi    

function prepare_env {
    env=$1
    if [ -d $env ] ; then
        echo Oops, a directory $env exists already.
        echo Delete it yourself if you dare!
        exit -1
    fi
    virtualenv $env
    . $env/bin/activate
    mkdir repositories
    cd repositories
}

function install {
    nickname=$1
    owner=$2
    repo=$3
    url=git@github.com:$owner/$repo.git
    # uncomment the following line if you want https remote
    # url=https://github.com/$owner/$repo.git
    if [ ! -d $nickname ] ; then
       git clone $url $nickname
    fi
    pip install -e $nickname
}


if [[ $1 ]] ; then
    prepare_env $1
fi

install cd lsaffre commondata
install be lsaffre commondata-be
install ee lsaffre commondata-ee
install eg lsaffre commondata-eg
install atelier lino-framework atelier
install lino lino-framework lino
install xl lino-framework xl
install noi lino-framework cosi
install presto lino-framework presto
install welfare lino-framework welfare
install voga lino-framework voga
install avanti lino-framework avanti
install book lino-framework book
install ext6 lino-framework extjs6

# the following are not really needed
install patrols lsaffre lino-patrols
install logos lsaffre lino-logos

