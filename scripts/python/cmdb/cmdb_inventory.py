#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import psycopg2
import csv
import subprocess
import sys
import os

stamp = time.strftime("%c")
repliexe = "sed 's/$/,,,,/g' /opt/vminventory/script/data_files/vm.dump.latest > /opt/vminventory/script/data_files/vms.csv"
chang = "sdiff -w285 /opt/vminventory/script/data_files/vms.bkp /opt/vminventory/script/data_files/vms.csv | grep '[<>]' > /opt/vminventory/script/data_files/compare.txt"
results = "printf '>ADDED\n---------\n' > /opt/vminventory/script/data_files/results.txt && grep '>' /opt/vminventory/script/data_files/compare.txt >> /opt/vminventory/script/data_files/results.txt && printf '\n<REMOVED\n-------------\n' >> /opt/vminventory/script/data_files/results.txt && grep '<' /opt/vminventory/script/data_files/compare.txt >> /opt/vminventory/script/data_files/results.txt"

repli_data = subprocess.Popen(repliexe, shell=True, stderr=subprocess.PIPE)
repli, err = repli_data.communicate()
print ("%s - Data replace error:" %stamp, repli)
print ("\n")
com_data = subprocess.Popen(chang, shell=True, stderr=subprocess.PIPE)
res_dat = subprocess.Popen(results, shell=True, stderr=subprocess.PIPE)

conn_db = "dbname='<DB-NAME>' user='<USER-NAME>'  host='localhost' password='<PASSWORD>'"
print ("%s - Opened DATABSE successfully.\n" %stamp)
conn = psycopg2.connect(conn_db)
cur = conn.cursor()
cur.execute("TRUNCATE TABLE <TABLE-NAME> CASCADE;")
conn.commit()
print ("%s - Table is empty now. Inserting new data.\n" %stamp)
print ("To check inventory, Please go to      URL: http://<IP-ADDRESS>/phppgadmin/ \nSelect  PostgreSQL --> cmdb(Database) --> public(Schema) --> machines(Table) --> Browse")

reader = csv.reader(open('/opt/vminventory/script/data_files/vms.csv', 'rb'))

for row in reader:
        statement = "INSERT INTO <TABLE-NAME> (Tenant_Id,Tenant_Name,Host_Id,Host,Created_Date,Status,Instance_Name,Keyname,Flavors,IP1,IP2,IP3,IP4) VALUES ('"+row[0]+"','"+row[1]+"','"+row[2]+"','"+row[3]+"','"+row[4]+"','"+row[5]+"','"+row[6]+"','"+row[7]+"','"+row[8]+"','"+row[9]+"','"+row[10]+"','"+row[11]+"','"+(row[12])+"')"
        cur.execute(statement)
        conn.commit()

with open("/opt/vminventory/script/data_files/results.txt", "r") as f:
        print ("\n")
        print f.read()

