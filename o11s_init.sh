#!/bin/bash
#---- Sample open802.11s Initialization script for a board with 3x Wi-Fi Radios ----
PHY0=`cat /sys/class/net/wlan0/phy80211/name`
PHY1=`cat /sys/class/net/wlan1/phy80211/name`
PHY2=`cat /sys/class/net/wlan2/phy80211/name`
#-------------------------
iw wlan0 del
iw phy $PHY0 interface add mesh0 type mp mesh_id PANDA36
iw dev mesh0 set channel 36 HT40+
ifconfig mesh0 up
#-------------------------
iw wlan1 del
iw phy $PHY1 interface add mesh1 type mp mesh_id PANDA40
iw dev mesh1 set channel 40 HT40+
ifconfig mesh1 up
#-------------------------
iw wlan2 del
iw phy $PHY2 interface add mesh2 type mp mesh_id PANDA6
iw dev mesh2 set channel 6 HT40+
ifconfig mesh2 up
