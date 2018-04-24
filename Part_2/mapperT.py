#!/usr/bin/env python3
"""mapperT.py"""

import sys
import json
pronouns = ['han','hon','den','det','denna','denne','hen']
# input comes from STDIN (standard input) load into json
for line in sys.stdin:
	try:
		data = json.loads(line)
		text = json.dumps(data['text'])
		#print (text)
		text = text.strip().lower()
		words = text.split()
		for word in words:
			if (word in pronouns):
				print ('%s\t %s' % (word, 1))
		#print('\n')
	except:
		continue
