#!/usr/bin/env python
"""mapperT.py"""

import sys
import json

# input comes from STDIN (standard input) load into json
for line in sys.stdin:
   # jsonStr = line.decode("utf-8")
	try:
		data = json.loads(line)
		text = json.dumps(data['text'])
		print (text)
	except:
		continue
