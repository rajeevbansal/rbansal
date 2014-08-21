Subversion

This is the svn module.

Contact
-------
rajeev.bansal@rocketmail.com

Support
-------
rajeev.bansal@rocketmail.com

Note 
----
This module can be used to install and configure SVN (Subversion) Server on Fedora 20/19, CentOS/Red Hat (RHEL) 6.5/5.10 server on a rhel5/rhel6 hosts. 

After installing the subversion YOU can test with the following commands.

Add SVN (Subversion) users

Use following command:

## Create testuser ##
htpasswd -cm /etc/svn-auth-users testuser
New password: 
Re-type new password: 
Adding password for user testuser
 
## Create testuser2 ##
htpasswd -m /etc/svn-auth-users testuser2
New password: 
Re-type new password: 
Adding password for user testuser2
svnadmin create testrepo
chown -R apache.apache testrepo
 
 
## If you have SELinux enabled (you can check it with "sestatus" command) ##
## then change SELinux security context with chcon command ##
 
chcon -R -t httpd_sys_content_t /var/www/svn/testrepo
 
## Following enables commits over http ##
chcon -R -t httpd_sys_rw_content_t /var/www/svn/testrepo

Restart Apache:

## Fedora ##
systemctl restart httpd.service
## OR ##
service httpd restart
 
## CentOS / RHEL ##
/etc/init.d/httpd restart
## OR ##
service httpd restart
--------------------------------------------------------------------------------------------------------------

