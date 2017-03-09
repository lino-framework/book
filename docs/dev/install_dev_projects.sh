#!/bin/bash
set -e  # exit on error

function install(nickname, owner, repo) {
    url = git@github.com:$owner/$repo.git
    # uncomment the following line if you want https remote
    # url = https://github.com/$owner/$repo.git
    if [ ! -d $nickname ] ; then
       git clone $url $nickname
    fi
    pip install -e $nickname
}

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
install patrols lino-framework patrols
install logos lino-framework logos

