LocalYumServer

This is the local yum server module.

Contact
-------
rajeev.bansal@rocketmail.com

Support
-------
rajeev.bansal@rocketmail.com

Note 
----
This module can be used to Setup Local YUM Server in CentOS 6.x / RHEL 6.x.

Before setting up the local yum Server YOU would need to mount the contents of your CentOS 6.x/RHEL 6.x DVD. Follow the below steps to mount the Packages.

Use following command:

## Create testuser ##
mkdir -p /mnt/iso/

mount -o loop /opt/rajeev/isos/rhel-server-6.4-x86_64-dvd.iso /mnt/iso/

cd /mnt/iso/Packages/

##Restart Apache:##

## CentOS / RHEL ##
/etc/init.d/httpd restart
## OR ##
service httpd restart

--------------------------------------------------------------------------------------------------------------

