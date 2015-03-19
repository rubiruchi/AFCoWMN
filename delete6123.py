#!/bin/bash

#MR6
curl -X DELETE -d'{"name":"myflow1", "switch":"00:00:04:f0:21:11:3d:78"}' http://192.168.0.220:8080/wm/staticflowpusher/json
curl -X DELETE -d'{"name":"myflow2", "switch":"00:00:04:f0:21:11:3d:78"}' http://192.168.0.220:8080/wm/staticflowpusher/json
curl -X DELETE -d'{"name":"myflow3", "switch":"00:00:04:f0:21:11:3d:78"}' http://192.168.0.220:8080/wm/staticflowpusher/json
curl -X DELETE -d'{"name":"myflow4", "switch":"00:00:04:f0:21:11:3d:78"}' http://192.168.0.220:8080/wm/staticflowpusher/json

#MR1
curl -X DELETE -d'{"name":"myflow5", "switch":"00:00:04:f0:21:11:3d:86"}' http://192.168.0.220:8080/wm/staticflowpusher/json
curl -X DELETE -d'{"name":"myflow6", "switch":"00:00:04:f0:21:11:3d:86"}' http://192.168.0.220:8080/wm/staticflowpusher/json
curl -X DELETE -d'{"name":"myflow7", "switch":"00:00:04:f0:21:11:3d:86"}' http://192.168.0.220:8080/wm/staticflowpusher/json
curl -X DELETE -d'{"name":"myflow8", "switch":"00:00:04:f0:21:11:3d:86"}' http://192.168.0.220:8080/wm/staticflowpusher/json

#MR2
curl -X DELETE -d'{"name":"myflow9", "switch":"00:00:04:f0:21:11:3d:87"}' http://192.168.0.220:8080/wm/staticflowpusher/json
curl -X DELETE -d'{"name":"myflow10", "switch":"00:00:04:f0:21:11:3d:87"}' http://192.168.0.220:8080/wm/staticflowpusher/json
curl -X DELETE -d'{"name":"myflow11", "switch":"00:00:04:f0:21:11:3d:87"}' http://192.168.0.220:8080/wm/staticflowpusher/json
curl -X DELETE -d'{"name":"myflow12", "switch":"00:00:04:f0:21:11:3d:87"}' http://192.168.0.220:8080/wm/staticflowpusher/json

#MR3
curl -X DELETE -d'{"name":"myflow13", "switch":"00:00:04:f0:21:11:3d:74"}' http://192.168.0.220:8080/wm/staticflowpusher/json
curl -X DELETE -d'{"name":"myflow14", "switch":"00:00:04:f0:21:11:3d:74"}' http://192.168.0.220:8080/wm/staticflowpusher/json
curl -X DELETE -d'{"name":"myflow15", "switch":"00:00:04:f0:21:11:3d:74"}' http://192.168.0.220:8080/wm/staticflowpusher/json
curl -X DELETE -d'{"name":"myflow16", "switch":"00:00:04:f0:21:11:3d:74"}' http://192.168.0.220:8080/wm/staticflowpusher/json
