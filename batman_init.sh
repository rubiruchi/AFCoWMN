#!/bin/bash
#---- Sample Batman-adv Initialization script for a board with 3x Wi-Fi Radios ----
#---------------------Loading BATMAN-advanced kernel module------------------------
modprobe batman-adv
#insmod /lib/modules/3.13.0-non-pae/kernel/net/batman-adv/batman-adv.ko
PHY0=`cat /sys/class/net/wlan0/phy80211/name`
PHY1=`cat /sys/class/net/wlan1/phy80211/name`
PHY2=`cat /sys/class/net/wlan2/phy80211/name`
#----------1st interface configurationi (CH 36)-----------
iw wlan0 del
iw phy $PHY0 interface add wlan0 type ibss
ifconfig wlan0 mtu 1524 up
iw dev wlan0 ibss join PANDA36 5180 HT40+
batctl if add wlan0
#----------2nd interface configuration (CH 40)-----------
iw wlan1 del
iw phy $PHY1 interface add wlan1 type ibss
ifconfig wlan1 mtu 1524 up
iw dev wlan1 ibss join PANDA40 5200 HT40+
batctl if add wlan1
#----------3rd interface configuration (CH 48)-----------
iw wlan2 del
iw phy $PHY2 interface add wlan2 type ibss
ifconfig wlan2 mtu 1524 up
iw dev wlan2 ibss join PANDA6 2437 HT40+
batctl if add wlan2
ifconfig bat0 up
