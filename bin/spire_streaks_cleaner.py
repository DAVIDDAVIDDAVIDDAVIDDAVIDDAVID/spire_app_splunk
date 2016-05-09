#!/usr/bin/env python

import os, urllib2, json, datetime, ConfigParser


config_file = 'spire.conf'
config = ConfigParser.ConfigParser()
config.read(config_file)

url = 'https://app.spire.io/api/streaks'
date = ''
token = config.get('auth', 'token')
state = config.get('state', 'streaks')

req_string = url + '?access_token=' + token # + '&date=' + date

response = urllib2.urlopen(req_string).read()
streaks = json.loads(response)

latest = state

for streak in streaks:
    if streak['start_at'] > state:
#        print json.dumps(streak)
        if streak['start_at'] > latest:
            latest = streak['start_at']

print 'New latest: ' + str(latest)
