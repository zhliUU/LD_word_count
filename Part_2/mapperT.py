#!/usr/bin/env python3
"""mapperT.py"""

import sys
import json

# input comes from STDIN (standard input) load into json
for line in sys.stdin:
    data = json.load(line)
    print (data["text"])
