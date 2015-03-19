#! /usr/bin/python
import httplib
import json
 
class StaticFlowPusher(object):
 
    def __init__(self, server):
        self.server = server
 
    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])
 
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
 
    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200
 
    def rest_call(self, data, action):
        path = '/wm/staticflowpusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret
 
pusher = StaticFlowPusher('192.168.0.220')

#****************************************************************************************#
#MR6
flow1 = {
    'switch':"00:00:04:f0:21:11:3d:78",
    "name":"myflow1",
    "cookie":"0",
    "priority":"32768",
    "in_port":"3",
    "active":"true",
    "eth_type":"2048",
    "actions":"set_eth_dst=04:f0:21:11:3d:86,output=2"
    }
 
flow2 = {
    'switch':"00:00:04:f0:21:11:3d:78",
    "name":"myflow2",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "eth_type":"2048",
    "actions":"set_eth_dst=00:1e:8c:5a:55:da,output=3"
     }
flow3 = {
    'switch':"00:00:04:f0:21:11:3d:78",
    "name":"myflow3",
    "cookie":"0",
    "priority":"32768",
    "in_port":"3",
    "active":"true",
    "eth_type":"2054",
    "actions":"set_eth_dst=04:f0:21:11:3d:86,output=2"
    }

flow4 = {
    'switch':"00:00:04:f0:21:11:3d:78",
    "name":"myflow4",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "eth_type":"2054",
    "actions":"set_eth_dst=00:1e:8c:5a:55:da,output=3"
     }

#****************************************************************************************#
#MR1
flow5 = {
    'switch':"00:00:04:f0:21:11:3d:86",
    "name":"myflow5",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "eth_type":"2048",
    "actions":"set_eth_dst=04:f0:21:11:3d:89,output=1"
    }

flow6 = {
    'switch':"00:00:04:f0:21:11:3d:86",
    "name":"myflow6",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "eth_type":"2048",
    "actions":"set_eth_dst=04:f0:21:11:3d:78,output=2"
    }

flow7 = {
    'switch':"00:00:04:f0:21:11:3d:86",
    "name":"myflow7",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "eth_type":"2054",
    "actions":"set_eth_dst=04:f0:21:11:3d:89,output=1"
    }
flow8 = {
    'switch':"00:00:04:f0:21:11:3d:86",
    "name":"myflow8",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "eth_type":"2054",
    "actions":"set_eth_dst=04:f0:21:11:3d:78,output=2"
    }

#****************************************************************************************#
#MR2
flow9 = {
    'switch':"00:00:04:f0:21:11:3d:87",
    "name":"myflow9",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "eth_type":"2048",
    "actions":"set_eth_dst=e8:94:f6:24:a8:21,output=3"
    }

flow10 = {
    'switch':"00:00:04:f0:21:11:3d:87",
    "name":"myflow10",
    "cookie":"0",
    "priority":"32768",
    "in_port":"3",
    "active":"true",
    "eth_type":"2048",
    "actions":"set_eth_dst=04:f0:21:11:3d:88,output=1"
    }
flow11 = {
    'switch':"00:00:04:f0:21:11:3d:87",
    "name":"myflow11",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "eth_type":"2054",
    "actions":"set_eth_dst=e8:94:f6:24:a8:21,output=3"
    }

flow12 = {
    'switch':"00:00:04:f0:21:11:3d:87",
    "name":"myflow12",
    "cookie":"0",
    "priority":"32768",
    "in_port":"3",
    "active":"true",
    "eth_type":"2054",
    "actions":"set_eth_dst=04:f0:21:11:3d:88,output=1"
    }
#****************************************************************************************#
#MR5
flow13 = {
    'switch':"00:00:04:f0:21:11:3d:7b",
    "name":"myflow13",
    "cookie":"0",
    "priority":"32768",
    "in_port":"3",
    "active":"true",
    "eth_type":"2048",
    "actions":"set_eth_dst=04:f0:21:11:3d:72,output=2"
    }

flow14 = {
    'switch':"00:00:04:f0:21:11:3d:7b",
    "name":"myflow14",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "eth_type":"2048",
    "actions":"set_eth_dst=e8:de:27:1f:11:cd,output=3"
    }
flow15 = {
    'switch':"00:00:04:f0:21:11:3d:7b",
    "name":"myflow15",
    "cookie":"0",
    "priority":"32768",
    "in_port":"3",
    "active":"true",
    "eth_type":"2054",
    "actions":"set_eth_dst=04:f0:21:11:3d:72,output=2"
    }

flow16 = {
    'switch':"00:00:04:f0:21:11:3d:7b",
    "name":"myflow16",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "eth_type":"2054",
    "actions":"set_eth_dst=e8:de:27:1f:11:cd,output=3"
    }

#****************************************************************************************#
#MR4
flow17 = {
    'switch':"00:00:04:f0:21:11:3d:72",
    "name":"myflow17",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "eth_type":"2048",
    "actions":"set_eth_dst=04:f0:21:11:3d:75,output=2"
    }

flow18 = {
    'switch':"00:00:04:f0:21:11:3d:72",
    "name":"myflow18",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "eth_type":"2048",
    "actions":"set_eth_dst=04:f0:21:11:3d:7e,output=1"
    }
flow19 = {
    'switch':"00:00:04:f0:21:11:3d:72",
    "name":"myflow19",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "eth_type":"2054",
    "actions":"set_eth_dst=04:f0:21:11:3d:75,output=2"
    }

flow20 = {
    'switch':"00:00:04:f0:21:11:3d:72",
    "name":"myflow20",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "eth_type":"2054",
    "actions":"set_eth_dst=04:f0:21:11:3d:7e,output=1"
    }
#****************************************************************************************#
#MR3
flow21 = {
    'switch':"00:00:04:f0:21:11:3d:74",
    "name":"myflow21",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "eth_type":"2048",
    "actions":"set_eth_dst=00:1e:8c:5d:6c:84,output=3"
    }

flow22 = {
    'switch':"00:00:04:f0:21:11:3d:74",
    "name":"myflow22",
    "cookie":"0",
    "priority":"32768",
    "in_port":"3",
    "active":"true",
    "eth_type":"2048",
    "actions":"set_eth_dst=04:f0:21:11:3d:73,output=2"
    }
flow23 = {
    'switch':"00:00:04:f0:21:11:3d:74",
    "name":"myflow23",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "eth_type":"2054",
    "actions":"set_eth_dst=00:1e:8c:5d:6c:84,output=3"
    }

flow24 = {
    'switch':"00:00:04:f0:21:11:3d:74",
    "name":"myflow24",
    "cookie":"0",
    "priority":"32768",
    "in_port":"3",
    "active":"true",
    "eth_type":"2054",
    "actions":"set_eth_dst=04:f0:21:11:3d:73,output=2"
    }

pusher.set(flow1)
pusher.set(flow2)
pusher.set(flow3)
pusher.set(flow4)
pusher.set(flow5)
pusher.set(flow6)
pusher.set(flow7)
pusher.set(flow8)
pusher.set(flow9)
pusher.set(flow10)
pusher.set(flow11)
pusher.set(flow12)
pusher.set(flow13)
pusher.set(flow14)
pusher.set(flow15)
pusher.set(flow16)
pusher.set(flow17)
pusher.set(flow18)
pusher.set(flow19)
pusher.set(flow20)
pusher.set(flow21)
pusher.set(flow22)
pusher.set(flow23)
pusher.set(flow24)
