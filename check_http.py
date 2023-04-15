#!/bin/bash
 
curl -H "Content-Type: application/json" -d '{"clientip": "0.0.0.0", "cmdid": 123, "from": "xvision", "format": "json", "logid": 123123, "appid": "123456","data":"clcl"}' 'http://0.0.0.0:2002/v1/req'
