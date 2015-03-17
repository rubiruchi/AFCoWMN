#!/bin/bash

ip tuntap del tap0 mode tap
ovs-vsctl del-br br_wlan0
ovs-vsctl del-br br_wlan1
ovs-vsctl del-br br_wlan2
ovs-vsctl del-br br_tap

#create a virtual interface
ip tuntap add mode tap tap0

#create an ovs bridge for wlan0
ovs-vsctl add-br br_wlan0
ovs-vsctl add-port br_wlan0  wlan0
ovs-vsctl add-port br_wlan0  patch_wlan0_tap

#create an ovs bridge for wlan1
ovs-vsctl add-br br_wlan1
ovs-vsctl add-port br_wlan1  wlan1
ovs-vsctl add-port br_wlan1  patch_wlan1_tap

#create an ovs bridge for wlan2
ovs-vsctl add-br br_wlan2
ovs-vsctl add-port br_wlan2  wlan2
ovs-vsctl add-port br_wlan2  patch_wlan2_tap

#create an ovs bridge for tap0
ovs-vsctl add-br br_tap
ovs-vsctl add-port br_tap  tap0
ovs-vsctl add-port br_tap  patch_tap_wlan0
ovs-vsctl add-port br_tap  patch_tap_wlan1
ovs-vsctl add-port br_tap  patch_tap_wlan2

#set patch ports
ovs-vsctl set interface patch_tap_wlan0 type=patch
ovs-vsctl set interface patch_tap_wlan0 options:peer=patch_wlan0_tap
ovs-vsctl set interface patch_wlan0_tap type=patch
ovs-vsctl set interface patch_wlan0_tap options:peer=patch_tap_wlan0

ovs-vsctl set interface patch_tap_wlan1 type=patch
ovs-vsctl set interface patch_tap_wlan1 options:peer=patch_wlan1_tap
ovs-vsctl set interface patch_wlan1_tap type=patch
ovs-vsctl set interface patch_wlan1_tap options:peer=patch_tap_wlan1

ovs-vsctl set interface patch_tap_wlan2 type=patch
ovs-vsctl set interface patch_tap_wlan2 options:peer=patch_wlan2_tap
ovs-vsctl set interface patch_wlan2_tap type=patch
ovs-vsctl set interface patch_wlan2_tap options:peer=patch_tap_wlan2
                                                                         
                                                                         #setting DPIDs for bridges
ovs-vsctl set bridge br_tap other-config:datapath-id=0000000000000004
ovs-vsctl set bridge br_wlan0 other-config:datapath-id=0000000000000005
ovs-vsctl set bridge br_wlan1 other-config:datapath-id=0000000000000006
ovs-vsctl set bridge br_wlan2 other-config:datapath-id=0000000000000007


#set controller
ovs-vsctl set-controller br_tap tcp:192.168.0.220:6653
ovs-vsctl set controller br_tap connection-mode=out-of-band
#ovs-vsctl set-fail-mode br_tap standalone
#ovs-vsctl set bridge br_tap stp_enable=true


ovs-vsctl set-controller br_wlan0 tcp:192.168.0.220:6653
ovs-vsctl set controller br_wlan0 connection-mode=out-of-band
#ovs-vsctl set-fail-mode br_wlan0 standalone
#ovs-vsctl set bridge br_wlan0 stp_enable=true


ovs-vsctl set-controller br_wlan1 tcp:192.168.0.220:6653
ovs-vsctl set controller br_wlan1 connection-mode=out-of-band
#ovs-vsctl set-fail-mode br_wlan1 standalone
#ovs-vsctl set bridge br_wlan1 stp_enable=true

ovs-vsctl set-controller br_wlan2 tcp:192.168.0.220:6653
ovs-vsctl set controller br_wlan2 connection-mode=out-of-band
#ovs-vsctl set-fail-mode br_wlan2 standalone
#ovs-vsctl set bridge br_wlan2 stp_enable=true

#ifconfig lo up

# Disable IP Forwarding
echo "0" > /proc/sys/net/ipv4/ip_forward
echo "0" > /proc/sys/net/ipv4/conf/all/forwarding

ifconfig wlan0 down
ifconfig wlan1 down
ifconfig wlan2 down
ifconfig tap0 down
ifconfig br_wlan0 down
ifconfig br_wlan1 down
ifconfig br_wlan2 down

ip link set dev wlan0 promisc on up
ip link  set dev wlan1 promisc on up
ip link  set dev wlan2 promisc on up
ip link  set dev tap0 promisc on up
ip link  set dev tap0 promisc on up
ifconfig wlan0 0.0.0.0
ifconfig wlan1 0.0.0.0
ifconfig wlan2 0.0.0.0
ifconfig tap0 0.0.0.0

ifconfig br_wlan0 up
ifconfig br_wlan1 up

ifconfig tap0 up
ifconfig br_tap 10.11.12.2/24 up
