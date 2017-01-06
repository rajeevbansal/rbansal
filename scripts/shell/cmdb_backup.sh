#!/bin/sh

# What to backup.
backup_files="/opt/vminventory/script/data_files/vms.csv"

# Where to backup to.
dest="/opt/vminventory/script/data_files/backup/vms.copy"
path="/opt/vminventory/script/data_files/backup/"

# Print start status message.
echo "Backing up $backup_files to $dest"
date
echo
#Copying File
cp $backup_files $dest
cat /opt/vminventory/script/data_files/backup/vms.copy > /opt/vminventory/script/data_files/vms.bkp
cp /opt/vminventory/script/data_files/vms.bkp /opt/vminventory/script/data_files/backup/vms-`date -I`.backup
cp -vu /opt/vminventory/script/data_files/backup/*.backup /opt/vminventory/script/data_files/backup/latest
# Print end status message.
echo
echo "Backup finished"
date

ls -l $path
