Installing a WebDAV section
===========================

How to install :doc:`webdav` on apache.


- `How To Set Up WebDAV With Apache2 On Debian Etch <https://www.howtoforge.com/setting-up-webdav-with-apache2-on-debian-etch>`_

To allow WebDAV, add another `<Directory>` directive::
  
  <Directory /path/to/prj1/media/webdav/>
     DAV On
     ForceType text/plain
     AuthType Basic
     AuthName "Lino@Prj1"
     AuthUserFile /path/to/prj1/htpasswd/passwords
     AuthGroupFile /path/to/prj1/htpasswd/groups
     <LimitExcept GET>
     Require group dav
     </LimitExcept>
  </Directory>

Maybe also ``a2enmod dav_fs`` 


https://www.howtoforge.com/setting-up-webdav-with-apache2-on-debian-etch
