#!/usr/bin/python
import subprocess
import time
import MySQLdb
#---------------------------
db = MySQLdb.connect("localhost","root","D@woodmim0s","pandamesh")
cursor = db.cursor()
#---------------------------
while True:
        f1 = open('/root/aplist.txt')
        for AP_MIP in iter(f1):
                # Rading AP list line-by-line and Retreiving Router Information
                # pams-agent is "snmpwalk -v1 -c panlab2014 $AGENT_IP 1.3.6.1.4.1.8072.1.3.2.4.1.2 | awk -F\" '{print $2}'"
                command = "pms-agent " + AP_MIP
                out = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
                out.communicate()
                f2 = open('/root/output.txt')
                for line in iter(f2):
                        inp = line.rstrip('\n')
                        if ("10.11.12" in line):
                                ipadr = line.rstrip('\n')
                                print ipadr + " is added"
                        elif ("BI" in line):
                                print "Backhaul Info...."
                                imode,macw,txpwr,chl,mode,ess,rss,ctxr,lrxr,cntt,rxbs,rxdr,txbs,txrc,txrf,fcse,ofdme,bld = inp.split(" ")
                                SearchMBI = "SELECT * FROM MBI WHERE MACW=%s", (macw)
                                cursor.execute(*SearchMBI)
                                row = cursor.fetchone()
                                if row is None: # not exists
                                        InsertMBI = """INSERT INTO MBI (IPADR,MACW,TXPWR,CHL,MODE,ESS,RSS,CTXR,LRXR,CNTT,RXBS,RXDR,TXBS,TXRC,TXRF,FCSE,OFDME,BLD)
                                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                        %s,%s,%s,%s,%s,%s) """, (ipadr,macw,txpwr,chl,mode,ess,rss,ctxr,lrxr,cntt,rxbs,rxdr,txbs,txrc,txrf,fcse,ofdme,bld)
                                        try:
                                                cursor.execute(*InsertMBI)
                                                db.commit()
                                                print macw + " is inserted @ MBI Table ..."
                                        except:
                                                db.rollback()
                                                print "There is an Err0r to insert @ MBI Table !!!"
                                else:
                                        UpdateMBI = """UPDATE MBI SET TXPWR=%s,CHL=%s,MODE=%s,ESS=%s,RSS=%s,CTXR=%s,LRXR=%s,CNTT=%s,
                                        RXBS=%s,RXDR=%s,TXBS=%s,TXRC=%s,TXRF=%s,FCSE=%s,BLD=%s
                                        WHERE MACW=%s""", (txpwr,chl,mode,ess,rss,ctxr,lrxr,cntt,rxbs,rxdr,txbs,txrc,txrf,fcse,bld,macw)
                                        try:
                                                cursor.execute(*UpdateMBI)
                                                db.commit()
                                                print macw + " is updated @ MBI Table ..."
                                        except:
                                                db.rollback()
                                                print "There is an Err0r to update @ MBI Table !!!"
                        #------------------------------------
                        elif ("AI" in line):
                                print "Access   Info...."
                                imode,macw,txpwr,chl,mode,hwm,ssid,usrno,bld = inp.split(" ")
                                SearchMAI = "SELECT * FROM MAI WHERE MACW=%s", (macw)
                                cursor.execute(*SearchMAI)
                                row = cursor.fetchone()
                                if row is None: # not exists
                                        InsertMAI = """INSERT INTO MAI (IPADR,MACW,TXPWR,CHL,MODE,HWM,SSID,USRNO,BLD) 
                                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(ipadr,macw,txpwr,chl,mode,hwm,ssid,usrno,bld)
                                        try:
                                                cursor.execute(*InsertMAI)
                                                db.commit()
                                                print macw + " is inserted @ MAI Table ..."
                                        except:
                                                db.rollback()
                                                print "There is an Err0r to insert @ MAI Table !!!"
                                else:
                                        UpdateMAI = """UPDATE MAI SET TXPWR=%s,CHL=%s,MODE=%s,HWM=%s,SSID=%s,USRNO=%s,BLD=%s
                                        WHERE MACW=%s""", (txpwr,chl,mode,hwm,ssid,usrno,bld,macw)
                                        try:
                                                cursor.execute(*UpdateMAI)
                                                db.commit()
                                                print macw + " is updated @ MAI Table ..."
                                        except:
                                                db.rollback()
                                                print "There is an Err0r to update @ MAI Table !!!"
                        #---------------------------------------
                        else:
                                print "USERNO is " + usrno
                                if ( usrno != "0"):
                                        print "Station  Info...."
                                        umac,rssi,cntt,inac,rxbs,rxdr,txbs,txrc,txrf,ctxr,lrxr  = inp.split(" ")
                                        SearchSTA = "SELECT * FROM STA WHERE UMAC=%s", (umac)
                                        cursor.execute(*SearchSTA)
                                        row = cursor.fetchone()
                                        if row is None: # not exists
                                                InsertSTA = """INSERT INTO STA(IPADR,MACW,UMAC,RSSI,CNTT,INAC,RXBS,RXDR,TXBS,TXRC,TXRF,CTXR,LRXR) VALUES
                                                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(ipadr,macw,umac,rssi,cntt,inac,rxbs,rxdr,txbs,txrc,txrf,ctxr,lrxr)
                                                try:
                                                        cursor.execute(*InsertSTA)
                                                        db.commit()
                                                        print macw + " is inserted @ STA Table ..."
                                                except:
       db.rollback()
                                                        print "There is an Err0r to insert @ STA Table !!!"
                                        else:
                                                UpdateSTA = """UPDATE STA SET RSSI=%s,CNTT=%s,INAC=%s,RXBS=%s,RXDR=%s,TXBS=%s,TXRC=%s,TXRF=%s,CTXR=%s,LRXR=%s 
                                                WHERE UMAC=%s""", (rssi,cntt,inac,rxbs,rxdr,txbs,txrc,txrf,ctxr,lrxr,umac)
                                                try:
                                                        cursor.execute(*UpdateSTA)
                                                        db.commit()
                                                        print macw + " is updated @ STA Table ..."
                                                except:
                                                        db.rollback()
                                                        print "There is an Err0r to update @ STA Table !!!"
                f2.close()
                print "-------------------------------------"
        f1.close()
        time.sleep(5)
db.close()
