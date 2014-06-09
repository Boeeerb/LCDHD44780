# !/usr/bin/env python
# -*- coding: utf-8 -*-

import telnetlib;
import time;
import json
import urllib


host='127.0.0.1';
port='13666';
data = ""

tn = telnetlib.Telnet(host, port)
tn.write("hello\r");

data += tn.read_until("\n");
tn.write("screen_add G\n");
data += tn.read_until("\n");

tn.write("widget_add G 1 title\n");
data += tn.read_until("\n");

tn.write("widget_set G 1 \"TLBRC HapPi KS\"\n");
data += tn.read_until("\n");

tn.write("widget_add G 2 string\n");
data += tn.read_until("\n");

tn.write("widget_add G 3 string\n");
data += tn.read_until("\n");
pledged = ""
backers = ""

var = 1;
while var == 1 :
  response = urllib.urlopen('https://d2oher2uhvl0ur.cloudfront.net/projects/tlbrcandkre8/case4-kits-and-happi-robot-for-the-raspberry-pi/stats.json')
  k = json.load(response)
  backers = str(k["project"]["backers_count"])
  pledged = str(k["project"]["pledged"])

  tn.write("widget_set G 2 1 2 \"Backers: %s \"\n" % (backers))
  tn.write("widget_set G 3 1 3 \"Pledged: %s GBP \"\n" % (pledged[:-2]))
  data += tn.read_until("\n")
  time.sleep(120)
