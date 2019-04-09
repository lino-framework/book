#!/bin/bash
set -e  # exit on error

if [ "$1" = "-h"  -o "$1" = "--help" ]
then
    cat <<USAGE
Usage:
  $0 [ <envname> ]

When invoked with an envname, then it creates both that virtualenv and
a directory 'repositories'.

Without an envname it assumes that you want to install Lino into the
current virtualenv and that you are in your existing repositories
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

function install_them_all {

    install cd lsaffre commondata
    install be lsaffre commondata-be
    install ee lsaffre commondata-ee
    install eg lsaffre commondata-eg
    install atelier lino-framework atelier
    install etgen lino-framework etgen
    install lino lino-framework lino
    install xl lino-framework xl
    install cosi lino-framework cosi
    install noi lino-framework noi
    install voga lino-framework voga
    install avanti lino-framework avanti
    install vilma lino-framework vilma
    install care lino-framework care
    install tera lino-framework tera
    install amici lino-framework amici
    install book lino-framework book
    install ext6 lino-framework extjs6
    install openui5 lino-framework openui5
    install react lino-framework react

    # the following are needed e.g. to build Luc's blog
    install welfare lino-framework welfare
    install weleup lino-framework weleup
    install welcht lino-framework welcht
    install algus lino-framework algus
    install presto lino-framework presto
    install pronto lino-framework pronto
    install patrols lsaffre lino-patrols
    install logos lsaffre lino-logos
    install eid lino-framework eidreader

}


echo "You are about to install the Lino development environment"
if [[ $1 ]] ; then
    echo into new virtualenv $1
else
    echo into current virtualenv $ENV
    echo using repositories in `pwd`
fi

read -r -p "Are you sure? [y/N] " response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]
then
    if [[ $1 ]] ; then
        prepare_env $1
    fi
    install_them_all
else
    exit -1
fi

